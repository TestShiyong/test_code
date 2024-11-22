# import queue
import os
import time
from multiprocessing import Process, Queue
from multiprocessing import current_process
import requests

headers1 = {"Content-Type": "application/json", "x-token": "",
            "x-countryCode": 'us'}


def add_data():
    """
    生成数据 添加入队列

    :return:
    """
    url = 'https://api-t-9.azazie.com/1.0/user/register'
    data = [[url, "syt" + str(j) + '@tetx.com', '123456'] for j in range(20)]
    for i in data:
        que.put(i)
    print(current_process().name + "--end", que.qsize())


def func(queue):
    """
    如果 队列不为空 就调用注册接口
    :param queue:
    :return:
    """
    while queue.qsize() > 0:
        print('(ID{},JOB({}))'.format(os.getpid(), queue.qsize()))
        li_data = queue.get()
        data = {"email": li_data[1], "password": li_data[2]}
        print(data)
        res = requests.post(url=li_data[0], json=data, headers=headers1)
        print(res.json()['code'])


if __name__ == '__main__':

    que = Queue()
    li_que = []

    add_data()

    st = time.time()
    for i in range(4):
        process1 = Process(target=func, args=(que,))
        li_que.append(process1)

    for i in li_que:
        i.start()

    for i in li_que:
        i.join()
    en = time.time()
    print(en - st)
    print(1111)
