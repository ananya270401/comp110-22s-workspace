import numpy as np

x = np.arange(1, 5)
print(x[x % 2 == 1])
print(x.std())