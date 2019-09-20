import os
import time
import multiprocessing

def task(args):
    time.sleep(1)
    pid = os.getpid()
    return pid, args

start = time.time()
pool = multiprocessing.Pool(processes=6)
result = pool.map(task, range(10))
print(result)
print("Cost: {}".format(time.time() - start))
