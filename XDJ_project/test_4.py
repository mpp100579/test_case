# -*- coding:utf-8 -*-
import unittest, time, re
import HTMLTestRunner


class Test4(unittest.TestCase):
    def test_4(self):
        u"""初始化"""
        send(apduchange('F0100000100123456789abcdeffedcba9876543210'))
        send(apduchange('F014000000'))
        send(apduchange('F011000000'))
        send(apduchange('F01302c80908A000000151000000'))
        send(apduchange('F01302c2024428'))
        send(apduchange('F013028601C9'))
        send(apduchange('F015000000'))
        send(apduchange('00A4040000'))
        send(apduchange('00A4040012'))

        pass

        if __name__ == "__main__":
            testunit = unittest.TestSuite()
            testunit.addTest(Test4('test_4'))
            runner = unittest.TextTestRunner()
    #filename = 'C:\\result.html'
    #fp = file(filename,'wb')
    #runner = HTMLTestRunner.HTMLTestRunner(stream = fp, title = 'Report_title',description = 'Report_decription')
            runner.run(testunit)
        print 'finish test_4(initialization)'