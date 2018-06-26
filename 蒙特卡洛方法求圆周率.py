import random
import time
darts = 10000*10000
hits = 0
start =time.perf_counter()
for i in range(darts):
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    dist = pow(x**2+y**2,0.5)
    if dist<= 1:
        hits = hits +1
pi = 4 * (hits/darts)
print("圆周率π是{:.9}".format(pi))
print("运行时间是{:.5}".format(time.perf_counter()-start))
