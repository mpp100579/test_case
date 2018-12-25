# -*- coding:utf-8 -*-
from datetime import date

#1.设置条件；2.解析网页；3下载图片；4.保存信息
#http://www.7799520.com/api/user/pc/list/search?startage=21&endage=30&gender=2&cityid=180&marry=1&page=1



#设置条件:年龄
def query_age():
    age=int(input("请输入对方的年龄(如22)："))
    if 21<=age<= 30:
        startage=21
        endage=30
    elif 31<=age<=40:
        startage=31
        endage=40
    print (endage)
    return startage,endage
query_age()
'''
#设置条件:性别
def query_sex():
    sex= input("请输入对方的性别(如女):")
    if sex == '男':
        gender = 1
    else:
        gender = 2
    print(gender)
    return gender
query_sex()
'''
#设置条件：城市
def query_city():
    city = input("请输入城市名称：如武汉:")
    if city == '武汉':
        cityid = 180
    print(cityid)
    return cityid
query_city()




#设置条件：婚否


