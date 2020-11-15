from multiprocessing import Pool
import os
import time
import random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s run %0.2f seconds.' % (name, (end-start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(3)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Wainting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done')
