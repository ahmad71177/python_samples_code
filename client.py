# Import socket module 
import socket
import pickle

# Create a socket object 
client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
#print (f'Socket has been created successfully!')

#Connect to the server
HOST = socket.gethostname()
IP = socket.gethostbyname(HOST)
PORT = 1234
client.connect((IP,PORT))
print(f'Client Coneccted to the server!')

#Creating RFW request

#A random RFW_ID
RFW_ID = input('Enter an integer ID:')

#Benchmark type (such as DVDStore or NDBench)
BENCHMARK = input ('Choose a Benchmark type [DVDStore,NDBench]:')

#Workload Metric (such as CPU or NetworkIn or NetworkOut or Memory)
METRIC = input ('Choose a Workload Metric [CPU,NetworkIn,NetworkOut,Memory]:')

#Batch Unit (the number of samples contained in each batch, such as 100)
BATCH_UNIT = input ('Enter Batch Unit, such as 100:')

#Batch ID (such as the 1st or 2nd or… 5th Batch)
BATCH_ID = input ('Enter Batch ID, such as the 1st or 2nd or… 5th Batch:')

#Batch Size (such as the how many batches to return, 5 means 5 batches to return)
BATCH_SIZE = input ('Enter Batch Size, such as the how many batches to return, 5 means 5 batches:')

#create RFW request, serilize and send to server as an dictionary
RFW={
    'RFW_ID':int(RFW_ID),
    'BENCHMARK': BENCHMARK,
    'METRIC': METRIC,
    'BATCH_UNIT':int(BATCH_UNIT),
    'BATCH_ID':int(BATCH_ID),
    'BATCH_SIZE':int(BATCH_SIZE),
    }
#print (RFW)
#print (len(RFW)) #len before serilization

#serilize rfw with pickle
rfw_req = pickle.dumps(RFW)
#print(rfw_req)
#print (len(rfw_req))
#print (f'{len(rfw_req):<20}'+RFW['METRIC'])

#send rfw
client.send(rfw_req)
print('Waiting for server response ...')

data = client.recv(1024)
hdata = pickle.loads(data)
print(f'Server Response:\n{hdata}')

with open(f'received{RFW_ID}.csv', 'wb') as f:
    print ('Getting Samples...')
    
    while True:
        
        print('receiving data...')
        data = client.recv(1024)
        #print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)
print('Finishd!')
#close socket
#client.close()        

