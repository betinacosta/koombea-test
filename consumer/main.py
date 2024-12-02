import sys, os
from loguru import logger

from consumer import Consumer


logger.add(sys.stderr, level="INFO")


def main():
    consumer = Consumer()
    consumer.start_listening()
    logger.info('[*] Waiting for messages. To exit press CTRL+C')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
