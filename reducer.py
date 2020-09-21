import sys
import numpy as np
from sklearn.preprocessing import MinMaxScaler

attribute_values = []
for data in sys.stdin:
    data = data.strip()
    attribute_values.append(data)

attribute_values = np.array(attribute_values).astype(np.float)
attribute_values.sort()

min_attribute_value = attribute_values.min()
max_attribute_value = attribute_values.max()
mean_attribute_value = attribute_values.mean()
std_attribute_value = attribute_values.std()

print('Minimum: \t%s' % min_attribute_value)
print('Maximum: \t%s' % max_attribute_value)
print('Median: \t%s' % mean_attribute_value)
print('Standard Deviation: \t%s' % std_attribute_value)

print('Normalized samples:')
scaler = MinMaxScaler()
attribute_values = scaler.fit_transform(attribute_values.reshape(-1, 1))
print(*attribute_values, sep=", ")
