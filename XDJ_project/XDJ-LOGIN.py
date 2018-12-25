#coding=utf-8
#from this import d
import sys
import os

from selenium import webdriver
import selenium.webdriver.common.keys
from selenium.webdriver.common.action_chains import ActionChains#导入鼠标事件的类
from selenium.webdriver.common.keys import Keys  #需要引入keys包键盘使用方法
from selenium.webdriver.support.ui import WebDriverWait
from userdata import get_webinfo
#from log_module import Loginfo


def OpenBrower():                           #定义个打开浏览器函数，返回个浏览器句柄，定义后给别的函数调用
    webdriver_handle = webdriver.Firefox()  #选择一个浏览器
    return webdriver_handle                 #返回浏览器句柄给别的函数调用
def OpenUrl(handle ,url):                #定义打开URL函数，传入2个参数，一个是句柄一个是URL
    handle.get(url)                      #获取URL
    d.maximize_window()                  #打开网页后最大化


def findElement(d,arg):      #定义个查找元素函数，传入2个参数，d是句柄，arg是查找元素方式，供别的函数调用时可变长参数,可以是字典
    #*arg和 ** kwarg允许我们在调用函数的时候传入多个实参，*arg会把多出来的位置参数转化为tuple，**kwarg会把关键字参数转化为dict
    '''
    text_id:                 #自定义定位方式tex_id到点击登录框或者链接给变量ele_login
    userid:                  #自定义定位方式userid到用户名给变量userEle
    pwdid:                   #自定义定位方式pwdid到密码给变量pwdEle
    loginid:                 #自定义定位方式loginid到提交登录按钮给变量loginEle
    retrun useEle,pwdEle,loginEle  #返回定位3个元素的变量给别的函数调用
    '''
    if text_id in arg:                  #判断登录text_id是否存在，arg是查找元素方式，有的网页登录没有这个登录框或者按钮，
        ele_login =d.find_element_by_link_text(arg['text_id'])#by_link_text()后面带的是arg字典参数
        d.implicitly_wait(10) #隐性等待，查找到后等待10秒
        ele_login.click()#如果存在登录按钮就点击登录
    userEle=d.find_element_by_id(arg['userid'])#点击登录按钮后查找元素userid,pwdid,loginid赋值给相应变量
    pwdEle=d.find_element_by_id(arg['pwdid'])
    loginEle=d.find_element_by_id(arg['loginid'])
    return userEle,pwdEle,loginEle  #返回定位到了3个元素的位置字典给别的函数调用

def sendVals(eletuple,arg):#定义个输入数据的函数
    '''
    第一个参数:param tuple:  eletuple 元祖，定位元素放在元祖中
    第二个参数:param arg:   account:username,pwd 参数账号放在字典中，输入值放在arg字典中
    :return:
    '''
    listKey = ['username','pwd'] #输入值用列表接收
    i =0
    for key in listKey:
        eletuple[i].send_keys('')#输入为空字符串
        eletuple[i].clear()#清理一下
        eletule[i].send_keys(arg[key])#发送相应的数据，发送的是key对应的value，把所有的值都发进去了
        i+=1#索引加1
        eletuple[2].click()
def checkResult(d,text):
    try:
        d.find_element_by_link_text(text)
        print('account and pwd error!')
    except:
        print('account and pwd right!')

def login_test(ele_dict,user_list):     #函数的入口，登录
    d = OpenBrower()                    #加载浏览器
    OpenUrl(d ,dict['url'])             #加载URL
    ele_tuple = findElement(d, ele_dict)  # 调用查找函数findElement，拿到3个定位到的元素字典，把查找到的函数用return接收函数返回在tuple元祖中
    for arg in user_list: #用于判断循环,如果arg参数属于一组用户数参数的话
        sendVals(ele_tuple,arg)#调用sendVals函数,把定位元素定到了后和一组用户输入值发送
        checkRseult(d,ele_dict['errorid'])#检查输入值

if __name__=='__main__':
    url = 'http://www.maiziedu.com/'  # 定义真实的数据webinfo信息
    login_text = '登录'

    account = 'mazi-test@139.com' # 定义真实的数据userinfo信息
    pwd = 'bkc123456'
'''
    ele_dict = {'url':url,'text_id':login_text,'user_id':'id_account_1,'\
              'pwdid':'id_password_1','login_id':'login_btn','errorid':'请输入正确的用户名和密码' } #把查找和Web相关的元素，用字典ele_dict{元素变量：值}接收，字典
'''
ele_dict = get_webinfo(r'file://E:\python2.7.9\python_test\test_case\XDJ_project\webinfo.text')
uer_list=[{'username':account,'pwd':pwd}]#把和用户输入相关的用userlist列表接收，里面还是字典格式的用户信息
login_test(ele_dict,user_list)


print help(request)





