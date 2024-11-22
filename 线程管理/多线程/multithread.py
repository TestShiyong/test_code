import threading
from threading import Thread
from datetime import datetime
import time


def fun1():
    for i in range(6):
        time.sleep(1)
        # print(datetime.now())
        print('运行 fun1 方法')

def fun2():
    for i in range(3):
        time.sleep(1)
        # print(datetime.now())
        print('运行 fun2 方法')


#创建线程对象
t1 = threading.Thread(target=fun1, name='t-1')
t2 = threading.Thread(target=fun2, name='t-2')

start = time.time()
t1.start()
t2.start()
t2.join()
t1.join()
# t2.join()
print(111)
ent = time.time()
print(ent - start)
