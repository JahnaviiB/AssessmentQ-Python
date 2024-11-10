import time
import numpy as np

arr = np.arange(100000)
print(type(arr))

starta = time.time()
print(np.sum(arr))
enda = time.time()

print(enda - starta)


lst = list(range(0,100000))
startl = time.time()
print(type(lst))
print(sum(lst))
endl = time.time()
print(endl - startl)