# -*- coding:utf-8 -*-
"Combine tests for gnosis.xml.objectify package (req 2.3+)"
import unittest, doctest
#import test_2, test_3,test_4 #这里需要导入测试文件
import test_1, test_4 ,test_fasttest
import HTMLTestRunner
import time

suit=unittest.TestSuite()
#suit = doctest.DocTestSuite()
#将测试用例加入到测试容器中
suit.addTest(unittest.makeSuite(test_4.Test4))
suit.addTest(unittest.makeSuite(test_1.Test1))
suit.addTest(unittest.makeSuite(test_fasttest.Testfasttest))

#获取当前时间，这样便于下面的使用。
now = time.strftime("%Y-%m-%M-%H_%M_%S",time.localtime(time.time()))
#打开一个文件，将result写入此file中
fp=open("result"+now+".html",'wb')                  #打开一个文件，将result写入此file中，生成HTML文档

filename = 'C:\\result.html'
fp = file(filename, 'wb')


runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'BKC_XdjSys Test Report By测试部_MPP',description='BKY_XDJSYS/Login_Test') # 生成报告的Title,描述
runner.run(suit)                                #执行容器中的测试用例