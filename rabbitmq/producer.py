#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost'))
channel = connection.channel()
queue_name = 'web-crawler-results'
channel.queue_declare(queue=queue_name)
channel.basic_publish(exchange='',
                      routing_key=queue_name,
                      body='Hello World @ {}'.format(time.time()))
print('producer: sent message')
connection.close()
