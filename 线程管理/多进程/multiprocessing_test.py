from multiprocessing import Process
import os

a = 0


def func():
    print('子进程({})开始运行'.format(os.getpid()))
    global a
    for i in range(1000):
        a += 1
    print('子进程({})任务执行完毕'.format(os.getpid()))

def func2():
    print('子进程({})开始运行'.format(os.getpid()))
    global a
    for i in range(1000):
        a += 1
    print('子进程({})任务执行完毕'.format(os.getpid()))

def func3():
    print('子进程({})开始运行'.format(os.getpid()))
    global a
    for i in range(1000):
        a += 1
    print('子进程({})任务执行完毕'.format(os.getpid()))


if __name__ == '__main__':
    print('主进程（{}）'.format(os.getpid()))
    process1 = Process(target=func)
    process2 = Process(target=func2)
    process3 = Process(target=func3)
    process1.start()
    process2.start()
    process3.start()
