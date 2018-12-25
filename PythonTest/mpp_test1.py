#coding:utf-8
from xlwt import *

# 需要xlwt库的支持
# import xlwt
file = Workbook(encoding='utf-8')
# 指定file以utf-8的格式打开
table = file.add_sheet('data')
# 指定打开的文件名
data = {
    "1": ["张三", 150, 120, 100],
    "2": ["李四", 90, 99, 95],
    "3": ["王五", 60, 66, 68]
}
for a in data:
    print a
num = [a for a in data]
print num

ldata = []
for x in num:#通过字典的每个key值打印key和值？
    # for循环将data字典中的键和值分批的保存在ldata中
    t = [int(x)]
    for a in data[x]:
        t.append(a)
    ldata.append(t)
print t
print ldata
for i, p in enumerate(ldata):
    # 将数据写入文件,i是enumerate()函数返回的序号数
    for j, q in enumerate(p):
        # print i,j,q
        table.write(i, j, q)
file.save('data1.xlsx')


import logging
# 创建一个logger
logger = logging.getLogger('这个模块的方法打印日志')

logger1 = logging.getLogger('mylogger')
logger1.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log')

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()

# 定义handler的输出格式formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 给logger添加handler
#logger.addFilter(filter)

logger.addHandler(fh)
logger.addHandler(ch)

# logger1.addFilter(filter)
logger1.addHandler(fh)
logger1.addHandler(ch)

logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')

logger1.debug('logger1 debug message')
logger1.info('logger1 info message')
logger1.warning('logger1 warning message')
logger1.error('logger1 error message')
logger1.critical('logger1 critical message')