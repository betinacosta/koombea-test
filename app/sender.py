import json

import pika, sys, os
from loguru import logger
from dotenv import load_dotenv

load_dotenv()
logger.add(sys.stderr, level="INFO")

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST')
RABBITMQ_PORT = os.getenv('RABBITMQ_PORT')
QUEUE = os.getenv('QUEUE')

class Sender:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=QUEUE)

    def send(self, event):
        self.channel.basic_publish(exchange='',
                              routing_key=QUEUE,
                              body=json.dumps(event.body))
        logger.info(f"Sent event {event.body['event_id']} to {QUEUE}")
        self.connection.close()