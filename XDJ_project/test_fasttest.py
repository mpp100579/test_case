# -*- coding:utf-8 -*-
#..实现接口
import unittest
class Testfasttest(unittest.TestCase):                        #其中一个测试类，继承父类单元测试用例
    def test_fasttest(self):                                  #方法test_fasttest(self):
        #...测试案例（各种算法）
        if __name__ == "__main__":                               #待执行的代码行
            testunit = unittest.TestSuite()                        #加载测试集
            testunit.addTest(Testfasttest('test_fasttest'))     #把测试用例加载到测试集中
            runner = unittest.TextTestRunner()                 #加载测试执行RUNNER,unittest.TestRunner
            #filename = 'C:\\result.html'
            #fp = file(filename,'wb')
            #runner = HTMLTestRunner.HTMLTestRunner(stream = fp, title = 'Report_title',description = 'Report_decription')
            runner.run(testunit)                                #启动执行测试集  runner.run
    print'finish test_fasttest'