import json
from logging import DEBUG

import pika
from loguru import logger

logger.add('logs/logs.log', level='DEBUG')


class Sender:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='koombea_queue')

    def send(self, event):
        self.channel.basic_publish(exchange='',
                              routing_key='koombea_queue',
                              body=json.dumps(event.body))
        logger.info(f"Sent event {event.body['event_id']} to koombea_queue")
        self.connection.close()