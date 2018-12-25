# coding=utf-8
import re
import sys
import time

import requests
from lxml import etree

import importlib
print dir(importlib)
print help(importlib)

#importlib.reload(sys)


# 定义一个爬虫
class spider(object):
    def __init__(self):
        print('开始爬取内容。。。')

    # getsource用来获取网页源代码
    def getsource(self, url):
        html = requests.get(url)
        return html.text

    # changepage用来生产不同页数的链接
    def changepage(self, url, total_page):
        if re.search('index_(\d+)', url, re.S):
            now_page = int(re.search('index_(\d+)', url, re.S).group(1))  # 可修改
        else:
            now_page = 0
        page_group = []
        for i in range(now_page, total_page + 1):
            link = re.sub('index_\d+', 'index_%s' % i, url, re.S)  # 可修改
            page_group.append(link)
        return page_group

    # getpic用来爬取一个网页图片
    def getpic(self, source):
        selector = etree.HTML(source)
        pic_url = selector.xpath('//ul[@class="ali"]/li/div/a/img/@src')  # 可修改
        return pic_url

    # savepic用来保存结果到pic文件夹中
    def savepic(self, pic_url):
        picname = re.findall('(\d+)', link, re.S)  # 可修改
        picnamestr = ''.join(picname)
        i = 0
        for each in pic_url:
            print('now downloading:{}'.format(each))
            pic = requests.get(each)
            fp = open('pic\\' + picnamestr + '-' + str(i) + '.jpg', 'wb')
            fp.write(pic.content)
            fp.close()
            i += 1

            # ppic集合类的方法

    def ppic(self, link):
        print('正在处理页面：{}'.format(link))
        html = picspider.getsource(link)
        pic_url = picspider.getpic(html)
        picspider.savepic(pic_url)


if __name__ == '__main__':
    start = time.time()
    url = 'http://www.baidu.com/'  # 可修改
    picspider = spider()
    all_links = picspider.changepage(url, 3)  # 可修改
    for link in all_links:
        picspider.ppic(link)
    end = time.time()
    print('耗时:{}'.format(start - end))