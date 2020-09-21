import sys
import numpy as np
from sklearn.preprocessing import MinMaxScaler

attribute_values = []
for data in sys.stdin:
    data = data.strip()
    attribute_values.append(data)

attribute_values = np.array(attribute_values).astype(np.float)
attribute_values.sort()

#calc percentile 90th, array should be sorted
per90th_value = np.percentile(attribute_values, 90)
#calculate the 90% percentile data
z = np.array(attribute_values)
lenght = np.shape(z)
a = 0.9 * lenght[0]
#New data thai is 90% percentile of data
attribute_values = z [:round(a)]
#calculate the min,Max,std,median and normalized
min_attribute_value = attribute_values.min()
max_attribute_value = attribute_values.max()
mean_attribute_value = attribute_values.mean()
std_attribute_value = attribute_values.std()

print('Minimum90percentile: \t%s' % min_attribute_value)
print('Maximum90percentile: \t%s' % max_attribute_value)
print('Median90percentile: \t%s' % mean_attribute_value)
print('Standard Deviation90percentile: \t%s' % std_attribute_value)
print(f'90th Percentile:\t {per90th_value}')

print('Normalized samples90percentile:')
scaler = MinMaxScaler()
attribute_values = scaler.fit_transform(attribute_values.reshape(-1, 1))
print(*attribute_values, sep=", ")
