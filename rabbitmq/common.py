import pika
import mysql.connector
import json
import db_settings


class RabbitMqQueue:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.name = 'web-crawler-results'
        self.channel.queue_declare(queue=self.name)
        self.db = DB()

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
        data = json.loads(body)
        self.db.insert_url(data['url'])

    def close(self):
        self.connection.close()


class DB:
    def __init__(self):
        self.cnx = mysql.connector.connect(
            host=db_settings.HOST,
            user=db_settings.USER, password=db_settings.PASSWORD,
            database=db_settings.DATABASE)

    def insert_url(self, url):
        cursor = self.cnx.cursor()
        cursor.execute(
            'INSERT INTO crawled_urls (url) VALUES (%s)', (url,))
        self.cnx.commit()
        cursor.close()
