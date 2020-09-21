#!/usr/bin/env python3

#built-in socket module
import socket
import pickle
import csv


#creating socket object
# AF_INET => IPv4
#SOCK_STREAM => TCP
server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)  
print ('Server Socket created successfully!')

#binding socket to host and port
#host and port
HOST = socket.gethostname()
IP = socket.gethostbyname(HOST)
PORT = 1234
server.bind((IP,PORT))
print(f'Socket binded to host={IP} and port={PORT}')

#listen to that socket
#listens for 1 active connection.
#This number can be increased as per convenience. 
server.listen(5)

conn = None

while True:
    
    #if we have no connection
    if conn is None:
        
        print ('Waiting for new connection...')
        #clientsocket connection
        conn, addr = server.accept()
        print(f'Connected by {addr}')
        
    else:
         
        #if conn ok then first get the rfw req
        rfw_req = conn.recv(1024)
        rfw= pickle.loads(rfw_req)
        #print (rfw['METRIC'])
        RFW_ID = rfw['RFW_ID']
        BENCHMARK = rfw['BENCHMARK']
        METRIC = rfw['METRIC']
        BATCH_UNIT = rfw['BATCH_UNIT']
        BATCH_ID = rfw['BATCH_ID']
        BATCH_SIZE = rfw['BATCH_SIZE']
        #print(METRIC)

        #open file and do our best!
        with open (BENCHMARK+'.csv') as csvfile:

            #You can read the header by using the next() function
            #which return the next row of the reader’s iterable object as a list.
            #then you can add the content of the file to a list.
                
            reader = csv.reader(csvfile, delimiter=',')
            header = next(reader) #first row , column names, next the reader!
            #print(header)
            #['CPUUtilization_Average', 'NetworkIn_Average', 'NetworkOut_Average', 'MemoryUtilization_Average', 'Final_Target']
                
            #ValueError: I/O operation on closed file.

            #row count except first row! 
            ROW_COUNT = sum(1 for row in reader)
            #print(ROW_COUNT)

        csvfile.close()
        #inja dg file close shode!!! chon 'with' tamum shod

        #int division
        unit= ROW_COUNT//BATCH_UNIT
        print(f'There are {BATCH_UNIT} samples in each {unit} batches!' )

        #start row of nth batch ex, 2nd batch => 2*batch_unit => row[200]
        start_row = BATCH_ID * BATCH_UNIT
        print(f'Start Row = {start_row}')

        #end_row means how many rows should transfer from start row, 5*100 = 500 + row[200] = row[700]
        end_row = (BATCH_SIZE * BATCH_UNIT)+ start_row
        print(f'End Row = {end_row}')
                    
        #LAST BATCH ID => 700 // 100 => 7
        LAST_BATCH_ID = end_row // BATCH_UNIT
        print(f'Last Batch ID = {LAST_BATCH_ID} ')

        #create rfd file to send client
        with open(f'rfd{RFW_ID}.csv', 'w',newline= '') as rfdfile:
                
            writer = csv.writer(rfdfile,dialect='excel')
            #first row, put [] A string happens to be a sequence of strings too, but it's a sequence of 1 character strings,
            #which isn't what you want.
            writer.writerow([METRIC])
                
            #open file again for iteration
            with open (BENCHMARK+'.csv') as csvfile:

                reader = csv.reader(csvfile, delimiter=',')
                header = next(reader) 

                    
                for index, row in enumerate(reader):
                    if index in range(start_row-1,end_row):
                        #print(index,row)
                        if METRIC == 'CPU':
                            writer.writerow([row[0]])
                            #print (row[0])
                        if METRIC == 'NetworkIn':
                            #writer.writerow(row[1])
                            writer.writerow([row[1]])
                            #print (row[1])
                        if METRIC == 'NetworkOut':
                            writer.writerow([row[2]])
                            #print (row[2])
                        if METRIC == 'Memory':
                            writer.writerow([row[3]])
                            #print (row[3])
                                
            csvfile.close()
                
        rfdfile.close()


        #send some init text
        conn.send(pickle.dumps(f'RFW ID ={RFW_ID}\nLast Batch ID = {LAST_BATCH_ID}'))

        #now send this file to client!
        with open(f'rfd{RFW_ID}.csv', 'rb') as f:
            data = f.read(1024)
            while data:
                conn.send(data)
                data = f.read(1024)


        conn=None

                             
