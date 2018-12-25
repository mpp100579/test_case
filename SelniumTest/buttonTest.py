#coding=utf-8

from selenium import webdriver
'''
import selenium.webdriver.common.keys
from selenium.webdriver.common.action_chains import ActionChains#导入鼠标事件的类
from selenium.webdriver.common.keys import Keys  #需要引入keys包键盘使用方法
from selenium.webdriver.support.ui import webDriverWait


#鼠标操作事件：还是先定位，再用ActionChains(driver)生成模拟用户行为，比如鼠标的5种操作方法，context_click ; double_click ;
#drag_and_drop ; move_to_element() ; click_and_hold
driver.maximize_window()

ele = driver.find_element_by_link_text('机器学习')
ActionChains(driver).move_to_element(ele).perform()
ele.click()
driver.back()
ele1=driver.find_element_by_css_selector('img[alt = \'UI设计保就业课程\']')
ActionChains(driver).move_to_element(ele1).perform()
ele1.click()

ele = driver.find_element_by_class_name('data-search font12')
ele.clear()
ele.send_keys('python1')
ele.send_keys(Keys.CONTROL,'A')
ele.send_keys(Keys.CONTROL,'X')
ele.send_keys(Keys.CONTROL,'V')
'''





driver = webdriver.Firefox()
driver.get('http://www.maiziedu.com/')
