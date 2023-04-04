import time
from multiprocessing import Process, Queue
from threading import Thread
import gevent
from gevent import monkey
import requests


def pro_work(que, pname):
    li_thr = []
    # 创建5个线程
    for i in range(1, 6):
        t_name = '线程({})'.format(i)
        li_thr.append(Thread(target=thr_work, args=(que, t_name,)))
        print('{}:创建线程({})成功'.format(pname, t_name))

    # 运行线程
    for i in li_thr:
        i.start()
    # 阻塞 进程 等待线程
    for i in li_thr:
        i.join()


def thr_work(que, t_name):
    li_gev = []
    # 创建5个协成
    for j in range(1, 6):
        g_name = '协成({})'.format(j)
        print('{}:创建协程({})成功'.format(t_name, g_name))
        li_gev.append(gevent.spawn(gev_work, que, g_name))
    # 运行协成 阻塞 线程 等待协成
    gevent.joinall(li_gev)


def gev_work(que, g_name):
    a = 0
    while not que.empty():
        try:
            value = que.get(timeout=0.01)
        except:
            print('超时')
        gevent.sleep(0.001)
        print(g_name + ' run job ({}) 次 value ({})'.format(a, value))
        a += 1


def mian():
    # 创建线程通信队列
    li_pro_obj = []
    que = Queue()

    # 队列添加10000个任务
    for i in range(10000):
        que.put(i)

    # 创建线程对象
    for i in range(1, 3):
        pname = '进程程({})'.format(i)
        li_pro_obj.append(Process(target=pro_work, args=(que, pname)))
        print('创建进程成功({})'.format(pname))

    # 运行进程
    for i in li_pro_obj:
        i.start()

    # 阻塞主进程 等待子进程
    for i in li_pro_obj:
        i.join()


if __name__ == '__main__':
    st = time.time()
    mian()
    et = time.time()
    print(et - st)
