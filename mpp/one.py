# -*- coding:utf-8 -*-
import time
from selenium import webdriver

br = webdriver.Chrome()
br.maximize_window()
br.get('http://192.168.1.56:81')
time.sleep(3)

def test_login(self):
    title = self.br.title
    print title
    now_url = self.br.url
    print now_url
    title = br.title
    print title
    username = "yujian"
    password = "bkc123456"
    # 用户名的定位
    br.find_element_by_id("uid").clear()
    br.find_element_by_id("uid").send_keys(username)
    # 密码的定位
    br.find_element_by_id("paw").clear()
    br.find_element_by_id("paw").send_keys(password)
    # 点击登录
    br.find_element_by_class_name("btn btn-lg btn-info btn-block text-base").click()
    # 登录成功断言
    str1 = '主页'
    str2 = br.find_element_by_xpath('/html/body/div[1]/header/div/ul/li[1]/a').text
    return str2
    assert str1 == str2
    # login_name = login_name.strip('您好：')
    assert login_name == username

def baidu1():
    # 用户名的定位
    br.find_element_by_id("uid").clear()
    br.find_element_by_id("uid").send_keys(username)
    # 密码的定位
    br.find_element_by_id("paw").clear()
    br.find_element_by_id("paw").send_keys(password)
    # 点击登录
    br.find_element_by_class_name("btn btn-lg btn-info btn-block text-base").click()
    # 登录成功断言
    str1='主页'
    str2 = br.find_element_by_xpath('/html/body/div[1]/header/div/ul/li[1]/a').text
    return str2
    assert str1==str2
   #login_name = login_name.strip('您好：')
    assert login_name == username


def baidu2():

    jg = br.find_element_by_id('jgwab').text
    return jg