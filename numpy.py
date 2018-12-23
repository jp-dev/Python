''' Test file
'''

import numpy as np

a = np.array([1, 2, 3, 4])
a + 1

2**a



b = np.ones(4) + 1
a - b

a * b


j = np.arange(5)
2**(j + 1) - j


a = np.arange(10000)
%timeit a + 1  

l = range(10000)
%timeit [i+1 for i in l] 


c = np.ones((3, 3))
c * c                   # NOT matrix multiplication!



c.dot(c)


