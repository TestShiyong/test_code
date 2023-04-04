import threading
import requests
import time

url = 'https://api-t-9.azazie.com/1.0/user/login'

data = {'email': 'shiyong1111@tetx.com',
        'password': '123456'}


count =0

class MyThread(threading.Thread):
    def __init__(self, url, data):
        self.data = data
        self.url = url
        super().__init__()

    # 重写了run方法  不需要去线程组对象入参 取方法 直接就运行了
    def run(self):
        global count
        for i in range(5):
            count+=1
            res = requests.post(url=url,json=data)
            print(threading.current_thread(),res.status_code)
            print('发送的第：{} 次请求'.format(i+1))

# 循环创建5个线程对象,放入列表
threads = [MyThread(url, data) for i in range(5)]
start_time = time.time()
# 遍历 线程对象运行
for i in threads:
    i.start()

# 遍历线程对象 同时每个线程都join等下
for j in threads:
    j.join()

ent_etime = time.time()
print('平均响应时间为： {}.'.format((ent_etime-start_time)/25))


