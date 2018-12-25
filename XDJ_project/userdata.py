#coding=utf-8
from os import path
from selenium import webdriver
import codecs
from selenium.webdriver.support.ui import WebDriverWait


def get_webinfo(path):
    web_info ={ }
   # config=open(path)
    config = codecs.open(path, 'r', 'utf-8')
    for line in config:
        result = [ele.strip() for ele in line.split('=')] #把带等号分割去掉变成列表
        web_info.update(dict([result])) #更新文件把列表转化字典
    return web_info
if __name__=='__main__':
    driver=webdriver.Firefox()
    info = driver.get(r'file:///E:\python2.7.9\python_test\test_case\XDJ_project\webinfo.text')
    for key in info:
        print (key ,info[key])
