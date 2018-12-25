# -*- coding:utf-8 -*-

import logging
import sys

logging.basicConfig(level=logging.DEBUG)#先设置日志级别
#logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Start reading database')
# read database here
records = {'john': 55, 'tom': 66}
logger.debug('Records: %s', records)

logger.info('Updating records ...')
# update records here
logger.info('Finish updating records')


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")





#可以通过向日志记录函数传递一个extra参数来实现向日志输出中添加额外的上下文信息，
fmt = logging.Formatter("%(asctime)s - %(name)s - %(ip)s - %(username)s - %(message)s")
h_console = logging.StreamHandler(sys.stdout)
h_console.setFormatter(fmt)
logger = logging.getLogger("myPro")
logger.setLevel(logging.DEBUG)
logger.addHandler(h_console)

extra_dict = {"ip": "113.208.78.29", "username": "Petter"}
logger.debug("User Login!", extra=extra_dict)

extra_dict = {"ip": "223.190.65.139", "username": "Jerry"}
logger.info("User Access!", extra=extra_dict)

#使用 FileHandler 把记录写进文件中：
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# create a file handler
handler = logging.FileHandler('hello.log')
handler.setLevel(logging.INFO)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)
logger.info('Hello baby')


import pdb

def make_bread():
    pdb.set_trace()
    return "I don't have time"
print(make_bread())