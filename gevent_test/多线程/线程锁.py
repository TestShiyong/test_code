import threading
import time

a = 0


def func1():
    global a

    for i in range(1000000):
        lock1.acquire()
        a += 1
        lock1.release()


def func2():
    global a

    for i in range(1000000):
        lock1.acquire()
        a += 1
        lock1.release()


lock1 = threading.Lock()
start_time = time.time()
t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)
t1.start()
t2.start()
t1.join()
t2.join()

end_time = time.time()
print(end_time - start_time)

print(a)
