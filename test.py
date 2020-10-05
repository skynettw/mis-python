import numpy as np 
import numpy.ma as ma

data = np.arange(25).reshape(5,5)
data += 245
data = ma.masked_where(data+3>255, data)
data += 3
ma.set_fill_value(data, 255)
data = ma.filled(data)
print(data)
