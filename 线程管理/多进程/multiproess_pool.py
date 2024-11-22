import os
import time
from multiprocessing import Pool, Manager, current_process
from multiprocessing import current_process
import requests


def add_data():
    """
    生成数据 添加入队列

    :return:
    """
    url = 'https://api-t-9.azazie.com/1.0/user/register'
    data = [[url, "syt" + str(j) + '@tetx.com', '123456'] for j in range(50)]
    for i in data:
        que.put(i)
    print(current_process().name + "--end", que.qsize())


def func(queue):
    """
    如果 队列不为空 就调用注册接口
    :param queue:
    :return:
    """
    headers1 = {"Content-Type": "application/json",
                "x-token": "",
                "x-countryCode": 'us'}

    while queue.qsize() > 0:
        print('(ID{},JOB({}))'.format(os.getpid(), queue.qsize()))
        li_data = queue.get()
        data = {"email": li_data[1], "password": li_data[2]}
        print(data)
        res = requests.post(url=li_data[0], json=data, headers=headers1)
        print(res.json()['code'])


if __name__ == '__main__':

    que = Manager().Queue()

    li_que = []

    add_data()

    st = time.time()
    pool = Pool(3)
    for i in range(3):
        pool.apply_async(func, args=(que,))

    pool.close()
    pool.join()
    en = time.time()
    print(en - st)
    print(1111)
