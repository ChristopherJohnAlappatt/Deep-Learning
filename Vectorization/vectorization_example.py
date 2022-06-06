import numpy as np
import time as time

n = 10000000

a = np.random.rand(n)
b = np.random.rand(n)
c = 0

start_time = time.time()
for i in range(n):
    c += a[i] * b[i]

end_time = time.time()
print(c)

t1 = end_time - start_time
print("Time taken using for-loop : " + str(t1 * 1000), "ms")

tic = time.time()
c = np.dot(a, b)
toc = time.time()
t2 = toc - tic
print(c)
print("Time taken using Vectorization : " + str(t2 * 1000), "ms")

speed_up_percentage = (t1 - t2) * 100 / t1
print("Speed up percentage", speed_up_percentage)
