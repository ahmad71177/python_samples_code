import sys

attribute_name = sys.argv[1]
data_type = sys.argv[2]
first_line = True
for line in sys.stdin:
    line = line.strip()
    data_values = line.split(",")
    data = 0.0
    if not first_line:
        if attribute_name == "CPUUtilization_Average":
            print('%s' % data_values[0])
        elif attribute_name == "NetworkIn_Average":
            print('%s' % data_values[1])
        elif attribute_name == "NetworkOut_Average":
            print('%s' % data_values[2])
        elif attribute_name == "MemoryUtilization_Average":
            print('%s' % data_values[3])
    else:
        first_line = False
        continue
