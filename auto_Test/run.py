# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
import time
import unittest

# 定义测试用例的目录为当前目录
test_dir = r'E:\test'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == "__main__":
    # 按照一定的格式获取当前的时间
    now = time.strftime("%Y-%m-%d %H-%M-%S")

    # 定义报告存放路径
    filename = test_dir + '/' + now + 'test_result.html'

    fp = open(filename, "wb")
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title=u"2100接口测试报告",
                            description=u"测试用例执行情况：")
    # 运行测试
    runner.run(discover)
    fp.close()  # 关闭报告文件