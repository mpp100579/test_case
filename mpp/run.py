# -*- coding:utf-8 -*-
import html
import three
import unittest

if __name__ == '__main__':
    # 调用定义HTMLTestRunner的方法
    runner = html.save_file()
    # 运行suite所组装的测试用例
    # runner = unittest.TextTestRunner()
    # 调用测试套件方法
    all_suite = three.all_suite()
    # 执行测试套件
    runner.run(all_suite)