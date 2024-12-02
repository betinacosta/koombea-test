import json
import pika, sys
import redis
import os
from loguru import logger
from dotenv import load_dotenv

load_dotenv()
logger.add(sys.stderr, level="INFO")

REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST')
RABBITMQ_PORT = os.getenv('RABBITMQ_PORT')
QUEUE = os.getenv('QUEUE')


class Consumer:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
        self.channel = self.connection.channel()

        self.channel.queue_declare(queue=QUEUE)

    @staticmethod
    def callback(ch, method, properties, body):
        redis_db = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
        event_item = json.loads(body.decode('utf-8'))

        logger.info(f"“Event {event_item.get('event_id')} has been sent to {event_item.get('user_id')}: {event_item.get('description')}.")
        logger.info(f"Storing {event_item.get('event_id')} on in memory database")

        redis_db.hset(f'event_id:{event_item.get("event_id")}', mapping={
            "user_id": event_item.get("description"),
            "description": event_item.get("description"),
            "status": event_item.get("status"),
            "event_id": event_item.get("event_id")
        })

    def start_listening(self):
        self.channel.basic_consume(
            queue=QUEUE,
            on_message_callback=self.callback,
            auto_ack=True
        )
        self.channel.start_consuming()
