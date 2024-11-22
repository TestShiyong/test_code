import gevent
from gevent import monkey
import time
import queue
import os
monkey.patch_all()

que = queue.Queue()




def test1():

    print('run test1 ：({})'.format(1))
    gevent.sleep(0.001)


def test2():
    print('run test2 ：({})'.format(1))
    gevent.sleep(0.001)

def test3():
    print('run test3 ：({})'.format(1))
    gevent.sleep(0.001)

for i in ['test1','test2','test3']:
    que.put(i)


g_obg = []
st = time.time()
# 创建 协成对象
for i in range(3):
    g_obg.append(gevent.spawn(que.get()))

for i in g_obg:
    i.start()

for i in g_obg:
    i.join()

# 协成存在线程之中  线程默认不会等待线程 需要用join进行线程阻塞
et = time.time()
print(et - st)
