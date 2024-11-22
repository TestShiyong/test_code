# 多线程模块
import threading
# 多线程队列
import queue as thr_que
import time
import os
# 多进程模块， 多进程共享资源队列
from multiprocessing import Process, queues as pro_que
# 线程池队列, 线程池
from multiprocessing import Manager, Pool

"""
5个线程 10万任务 14.9秒
li_thr = []

t_que = thr_que.Queue()

def func():
    while t_que.qsize()>0:
        print(threading.current_thread(),t_que.get())


for i in range(100000):
    t_que.put(i)


start_time = time.time()
for i in range(5):
    li_thr.append(threading.Thread(target=func))

for i in li_thr:
    i.start()

for i in li_thr:
    i.join()

end_time = time.time()
print(end_time -start_time)


"""


def work(q):
    print(q.get(), os.getpid())


if __name__ == '__main__':
    # p_que = pro_que.Queue()

    m_que = Manager().Queue()

    for i in range(100000):
        m_que.put(i)

    pool = Pool(5)
    while m_que.qsize() > 0:
        pool.apply_async(func=work, args=(m_que,))

    pool.close()
    pool.join()
