#!/usr/bin/env python
import time
import common

q = common.RabbitMqQueue()
try:
    q.publish('Hello World @ {}'.format(time.time()))
    print('producer: sent message')
finally:
    q.close()
