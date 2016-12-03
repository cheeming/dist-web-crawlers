import pika


class RabbitMqQueue:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.name = 'web-crawler-results'
        self.channel.queue_declare(queue=self.name)

    def publish(self, msg):
        self.channel.basic_publish(exchange='',
                                   routing_key=self.name,
                                   body=msg)

    def start_consuming(self):
        self.channel.basic_consume(self.receive_msg, queue=self.name,
                                   no_ack=True)
        self.channel.start_consuming()

    def receive_msg(self, ch, method, properties, body):
        print('ch: {}, method: {}, properties: {}, body: {}'.format(
            ch, method, properties, body))

    def close(self):
        self.connection.close()
