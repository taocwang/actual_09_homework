#coding:utf-8
import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(module)s %(lineno)d %(message)s",
                    filename="log.txt")

logging.info('i am info')
logging.warning('i am warmming')
logging.debug('i am debug')

