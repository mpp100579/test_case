# -*- coding:utf-8 -*-
import HTMLTestRunner
import time



def save_file():
    now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    fp = open("result" + now + ".html", 'wb')
    #filePath = "c:\\pyResult.html"
    #fp = file(filePath, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='BKC_XDJSys TestReport', description='Report_decription')
    return runner
print'finish html'