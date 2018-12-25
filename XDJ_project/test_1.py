# -*- coding:utf-8 -*-
import unittest, time, re
import HTMLTestRunner
from selenium import webdriver
import unittest
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')

class Test1(unittest.TestCase):
    # 指定浏览器
    def setUp(self):
        driver = webdriver.Firefox()
        driver.maximize_window()  # 将浏览器最大化显示
        time.sleep(5)
        # 打开url
        driver.get("http://192.168.1.56:81/")
        return driver

    # 登录操作
    def test_login(self):
        def setUp(driver):
            title = self.driver.title
            print title
            now_url = self.driver.current_url
            print now_url
            username = "yujian"
            password = "bkc123456"

            self.driver.find_element_by_id("uid").clear()
            self.driver.find_element_by_id("uid").send_keys(username)
            # 密码的定位
            self.driver.find_element_by_id("paw").clear()
            self.driver.find_element_by_id("paw").send_keys(password)
            # 点击登录
            self.driver.find_element_by_class_name("btn btn-lg btn-info btn-block text-base").click()
            # 登录成功断言
            login_name = self.driver.find_element_by_partial_link_text('/default/KPICenter').text
            login_name = login_name.strip('您好：')
            assert login_name == username

            # 关闭浏览器
    def tearDown(self):
        def setUp(driver):
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
    testunit = unittest.TestSuite()
    testunit.addTest(Test1('test_1'))
    runner = unittest.TextTestRunner()
    #filename = 'C:\\result.html'
    #fp = file(filename,'wb')
    #runner = HTMLTestRunner.HTMLTestRunner(stream = fp, title = 'Report_title',description = 'Report_decription')
    runner.run(testunit)
print 'finish test_1(login_pass)'