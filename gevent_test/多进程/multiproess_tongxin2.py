from multiprocessing import Process, Queue, current_process


"""
三个 进程程创建数据 添加到队列  全部添加完成后  调用gei方法取出三百个数据
"""
a= 0


def run(queue):
    # 64以及以下正常结束   65以及以上阻塞
    # 出问题数量似乎和put内容的大小有关
    for i in range(100):
        queue.put("123---")
    print(current_process().name + "--end")


def main():
    plist = []
    # 创建进程通信队列
    queue = Queue()
    # 创建进程对象 添加如列表
    for i in range(3):
        plist.append(Process(target=run, args=(queue,)))

    # 开启 三个线程，开始运行任务
    for i in plist:
        i.start()

    # 阻塞三个线程
    for i in plist:
        # 在这里被阻塞
        print(i.name + "----join")
        i.join()
    print(queue.qsize())
    global a

    # while not queue.empty():
    #     a+=1
    #     print(a)
    #     print(queue.get())





if __name__ == "__main__":
    main()
