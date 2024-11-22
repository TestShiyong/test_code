import queue
import threading
import time

que = queue.Queue()


class Output(threading.Thread):

    def run(self):
        while True:
            count = que.qsize()
            if count < 50:
                for i in range(200):
                    que.put('goods_' + str(i))
                print('已生产200个 等待2秒')
                time.sleep(2)


class Consume(threading.Thread):

    def run(self):
        while True:
            count = que.qsize()
            if count > 10:
                for i in range(3):
                    que.get()

            else:
                print('{} :消费剩余 小于10 等待两秒'.format(threading.current_thread()))
                time.sleep(2)


out_put = Output()
out_put.start()
for i in range(5):
    consme = Consume()
    consme.start()
