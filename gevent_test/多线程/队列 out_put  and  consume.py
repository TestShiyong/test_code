from gevent_test.multiThreading.queue_out_put import Output
from gevent_test.multiThreading.queue_consume import Consume

stock = 0

out_put = Output()
consume = Consume(out_put)

out_put.start()
# consume.start()


