# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from time import sleep

from selenium import webdriver
import unittest
import webbrowser
import time
import string
''''
url='http://192.168.1.56:81/'
driver = webdriver.Firefox()
driver.maximize_window()  # 将浏览器最大化显示
time.sleep(3)
# 打开url
driver.get(url)
print driver.title
if u'登录 - 巡检、点检、精密点检、检修一体化管理系统' == driver.title:               #断言
    print ('Assertion test pass.')
else:
    print ('Assertion test fail.')
current_time = time.strftime("%Y-%m-%d:%H_%M_%S", time.localtime(time.time()))
print(current_time )
nowTime=time.strftime('%Y%m%d.%H.%M.%S')
t=driver.get_screenshot_as_file('%s.jpg' %nowTime)          #截图
print (u'截图结果:%s'%t)
'''

class login(object):
    def __init__(self,username,password):
        self.username = username
        self.password = password

    url = '192.168.1.56:81'
    driver=webdriver.Firefox()
    driver.get(url)
    driver.maximize_window()
    def test_login(self):

        # 执行登录操作
        # 用户名的定位
        self.driver.find_element_by_id("uid").clear()
        self.driver.find_element_by_id("uid").send_keys(self.username)
        # 密码的定位
        self.driver.find_element_by_id("paw").clear()
        self.d.find_element_by_id("paw").send_keys(self.password)
        # 点击登录
        self.driver.find_element_by_class_name("btn btn-lg btn-info btn-block text-base").click()
        # 登录成功断言
        login_pass = self.driver.find_element_by_link_text('任务提醒')
        assert login_pass == '任务提醒'

if __name__ == '__main__':
    login_one=login('yujian','bkc123456')
    login_one.test_login()





'''
print string.center('打开浏览器1',60,'*')
url='https://blog.csdn.net/twc829/article/details/51787637'
webbrowser.open(url, new=0, autoraise=True)

print string.center('打开浏览器2',60,'*')
driver = webdriver.Firefox() #webdriver打开浏览器
#driver.get('https://huilansame.github.io')
driver.get("http://www.baidu.com")#get方法浏览器打开网页
driver.maximize_window()           #浏览器打开之后设置全屏
sleep(3)  # 强制等待3秒再执行下一步
print driver.current_url     #判断打印当前网页
print driver.title          #判断打印标题
ele1 = driver.find_element_by_class_name("s_ipt") #元素操作：浏览器定位元素
print ele1.id                           #打印id元素
e=ele1.send_keys("123")  #操作元素，输入方法输入

print string.center('打开浏览器3',60,'*')
driver = webdriver.Firefox() #webdriver打开浏览器
driver.get("http://www.maiziedu.com/")#get方法浏览器打开网页
driver.maximize_window()          #网页打开后设置全屏
ele2 = driver.find_element_by_link_text("机器学习")
ele2.click()

driver.back()                          #浏览器返回

print string.center('GUI编程',60,'*')
from Tkinter import *           # 导入 Tkinter 库
root = Tk()                     # 创建窗口对象的背景色
                                # 创建两个列表
li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
listb  = Listbox(root)          #  创建两个列表组件
listb2 = Listbox(root)
for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)

for item in movie:              # 第二个小部件插入数据
    listb2.insert(0,item)

listb.pack()                    # 将小部件放置到主窗口中
listb2.pack()
root.mainloop()                 # 进入消息循环

root = Tk.Tk()
root.title('测试窗口')
center_window(root, 300, 240)
root.maxsize(600, 400)
root.minsize(300, 240)
ttk.Label(root, relief=tk.FLAT, text='屏幕大小(%sx%s)\n窗口大小(%sx%s)' % (get_screen_size(root) + get_window_size(root))).pack(
    expand=tk.YES)
tk.mainloop()
'''
print string.center('GUI编程：大弹窗',60,'*')

from Tkinter import *
root = Tk()
root.title("hello world")
root.geometry('300x200')                 #是x 不是*

Label(root, text='校训', font=('Arial', 20)).pack()
frm = Frame(root)
#left
frm_L = Frame(frm)
Label(frm_L, text='厚德', font=('Arial', 15)).pack(side=TOP)
Label(frm_L, text='博学',font=('Arial', 15)).pack(side=TOP)
frm_L.pack(side=LEFT)

#right
frm_R = Frame(frm)
Label(frm_R, text='敬业', font=('Arial', 15)).pack(side=TOP)
Label(frm_R, text='乐群', font=('Arial', 15)).pack(side=TOP)
frm_R.pack(side=RIGHT)

frm.pack()

'''
root.resizable(width=False, height=True) #宽不可变, 高可变,默认为True
l = Label(root, text="show", bg="green", font=("Arial", 12), width=5, height=2)
l.pack(side=LEFT)  #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM

root.mainloop()
'''

print string.center('类测试',60,'*')
a=5
class A(object):
    def __init__(self, name,age):
        global a
        self.name=name
        self.age=age
    def setName(self):
        print 'A ' + self.name
    def setAge(self):
        return ('age  is :%s'%self.age)

class B(A):
    def __init__(self,name,age):
        super(B, self).__init__(name,age) #为了能使用或扩展父类的行为，最好显示调用父类的__init__方法,只调用了父类传参的的属性值
        print "hi"
        #self.name1 = name
        #self.age1=age
    def getName(self):
        n=setName()
        a=setAge()


if __name__=='__main__':
    b=B('feifei',20)
    print 'finished'


