import threading
import time

"""
多线程 不重写run方法
"""
def task(time_number):
    time.sleep(time_number)
    print(f'执行任务方法{time_number}秒')


def threadingBase():
    thead1 = threading.Thread(target=task, args=(3,))
    thead2 = threading.Thread(target=task, args=(5,))
    thead3 = threading.Thread(target=task, args=(5,))

    thead1.start()
    thead1.join()
    thead2.start()
    thead2.join()
    thead3.start()
    thead3.join()


# threadingBase()


"""
多线程 重新run方法 提升代码灵活型
"""
class MyThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        self.job1()
        self.job2()
        self.job3()

    def job1(self):
        print('job1')

    def job2(self):
        print('job2')

    def job3(self):
        print('job3')


# my_thread = MyThread('yong')
# my_thread.run()




"""
线程锁 手动锁应用
lock = threading.Lock()
lock.acquire()
lock.release()
多线程 资源共享 同时修改同一个资源 容易混乱 需要加上锁
"""
# numbers = 0
# lock = threading.Lock()
#
# def sum_data():
#     global numbers
#     lock.acquire()
#     for _ in range(10000000):
#         numbers += 1
#     lock.release()
#
#
# thread1 = threading.Thread(target=sum_data)
# thread2 = threading.Thread(target=sum_data)
# thread3 = threading.Thread(target=sum_data)
#
# thread1.start()
# thread2.start()
# thread3.start()
#
# thread1.join()
# thread2.join()
# thread3.join()
#
# print(numbers)





"""
推荐 
with 配合锁的使用

在Python中，with lock: 语句块实际上是使用了lock.acquire()和lock.release()来实现对锁的自动获取和释放。
当你使用 with lock: 时，Python会在进入 with 代码块之前自动调用 lock.acquire()，
在退出 with 代码块时自动调用 lock.release()。
"""

# numbers = 0
# lock = threading.Lock()
#
#
# def sum_data():
#     global numbers
#     with lock:
#         for _ in range(10000000):
#             numbers += 1
#
#
# thread1 = threading.Thread(target=sum_data)
# thread2 = threading.Thread(target=sum_data)
# thread3 = threading.Thread(target=sum_data)
#
# thread1.start()
# thread2.start()
# thread3.start()
#
# thread1.join()
# thread2.join()
# thread3.join()
#
# print(numbers)
