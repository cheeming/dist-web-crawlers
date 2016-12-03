#!/usr/bin/env python
import common

q = common.RabbitMqQueue()
try:
    print('Waiting for messages... To exit press CTRL+C')
    q.start_consuming()
finally:
    q.close()
