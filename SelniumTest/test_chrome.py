# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver
import webbrowser
import time
'''
url='https://blog.csdn.net/twc829/article/details/51787637'
webbrowser.open(url, new=0, autoraise=True)
'''
driver = webdriver.Chrome()
driver.get("http://zhaoyabei.github.io/")
driver.save_screenshot(driver.title+".png")


driver = webdriver.Chrome()
driver.get('http://www.51zxw.net/')
time.sleep(1)
print (driver.get_window_size())






driver.set_window_size(1280, 800)  # 分辨率 1280*800
time.sleep(1)
print (driver.get_window_size())

driver.set_window_size(1024, 768)  # 分辨率 1024*768
time.sleep(1)
print (driver.get_window_size())
