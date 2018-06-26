import time
print("-------进度条-------")
start = time.perf_counter()
for i in range(51):
    p = i * "*"
    k = "."*(50-i)
    d = time.perf_counter()- start
    print("\r{:3}%[{}{}]{:.2f}s".format(i,p,k,d),end="")
    time.sleep(0.1)