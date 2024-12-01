import pika
from loguru import logger

logger.add('logs/logs.log', level='DEBUG')

class Consumer:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()

        self.channel.queue_declare(queue='koombea_queue')

    @staticmethod
    def callback(ch, method, properties, body):
        logger.info(f"Received {body}")

    def start_listening(self):
        self.channel.basic_consume(
            queue='koombea_queue',
            on_message_callback=self.callback,
            auto_ack=True
        )
        self.channel.start_consuming()