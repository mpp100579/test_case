#coding=utf-8
import sys
import logging

logPath = r'./'
fileName = r'log'

# 创建logger对象
logger = logging.getLogger(name=__name__)
logger.setLevel(logging.DEBUG)

# 创建FileHandler对象
fileHandler = logging.FileHandler(r"{0}/{1}.log".format(logPath, fileName))
fileHandler.setLevel(logging.DEBUG)

# 创建formatter对象
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# 设置FileHandler对象格式
fileHandler.setFormatter(formatter)

# 把FileHandler对象添加到logger对像中
logger.addHandler(fileHandler)


# 代码部分
def test():
    logger.debug("debug message")
    logger.info("info message")
    logger.warn("warn message")
    logger.error("error message")
    logger.critical("critical message")


test()
