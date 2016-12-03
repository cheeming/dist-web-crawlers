#!/usr/bin/env python
import time
import common
import json

q = common.RabbitMqQueue()
try:
    data = json.dumps({
        'url': 'http://example.com/?{}'.format(time.time())
    })
    q.publish(data)
    print('producer: sent message')
finally:
    q.close()
