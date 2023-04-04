import queue

"""

# put 函数
# 当block 参数为False时 不在等待如果任务数 已满再添加就会报错

# 创建队列对象
# def __init__(self, maxsize=0)  最大传入任务数
# put 往队列里添加对象 当等待未Ture时 队列已满添加不会报错 因为在等待
que = queue.Queue(3)
que.put(11)
que.put(22)
que.put(33)
que.put(44, False)  # que.put(44, False) = que.put_nowait(44)


"""

# --------------------------------------------------------------------------------------------
que = queue.Queue(3)  # def __init__(self, maxsize=0)  最大传入任务数
que.put(11)  # def put(self, item, block=True, timeout=None) 是否等待  超时
que.put(22)
que.put(33)
print(que.get())
print(que.get())
print(que.get())

print(que.get())

# print(que.get(block=False))  # que.get(block=False) = que.get_nowait() 队列为空取 不等的会报错

# 获取当前 队列中的未取任务数
print(que.qsize())

# 判断当前队列是否已满
print(que.full())

# 判断当前队列是否为空
print(que.empty())

# 向队列发送一个信号 告诉队列一个任务已经完成 ，每个get（）都会调用都会得到一个任务，
que.task_done()
que.task_done()
que.task_done()
# que.join()
print('111111')



# -------------------------------------------------------------------------------------------

"""

# 后入先出队列
que = queue.LifoQueue()
que.put(11)
que.put(22)
que.put(33)

print(que.get())
"""


# que = queue.PriorityQueue()
# que.put((11,2))
# que.put((22,1))
# que.put((99,3))
# print(que.get())
# print(que.get())
# print(que.get())
