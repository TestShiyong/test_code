from 线程管理.multiThreading.queue_out_put import Output
from 线程管理.multiThreading.queue_consume import Consume

stock = 0

out_put = Output()
consume = Consume(out_put)

out_put.start()
# consume.start()


