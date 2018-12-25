#coding=utf-8

import threading
import time
import string
print string.center('习题1',60,'*')
a=[3,5,8]
print string.center('1.把28插入列表的末端',60,'-')
a.append(28)
print a

import requests
r = requests.get('https://www.douban.com/') # 豆瓣首页
print r.status_code
print r.text

'''
mlock=threading.RLock()

num = 500
def test(p):#被启动的线程函数带有一个参数P
    global num             #把赋值的全局变量传进来
    for i in xrange(0,100):#每个刷卡机每天被刷100次

        mlock.acquire()  #加锁
        num+=1          #要执行的代码，独占的操作
        mlock.release()  #释放锁
        time.sleep(0.005)
        print p


s=time.time()#时间方法
ts=[]
for i in xrange(0,10):#迭代是为了控制同时进行多少个线程和进程，循环10次
    th1=threading.Thread(target=test,args=[i])
    #th = threading.Thread(target=test, args=[i])
    th1.start()#启动线程
    #th.start()
    ts.append(th1)
    #ts.append(th)#把线程变成线程组

for i in ts:
    i.join()#等待上一个线程执行完，继续执行下一个线程

print '总账是%s块钱\n'%num
print "'i've finished!"

s=time.time()#时间方法
print 'time cost %s'%(time.time()-s)#程序执行需要用到的时间

print time.asctime( time.localtime(time.time()) )#打印当前时间

# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) 



import urllib2
def get_url(url):
    u=urllib2.urlopen(url).read()
    re_title='<title>(.*)</title>'
    title=re.findall(re_title,u)#findall取出来
    print title[0],u

urlinfo=['http://www.sohu.com','http://www.163.com','http://www.sina.com']
thr_list=[]
for i in range(0,len(urlinfo)):
    th1=threading.Thread(target=get_url,args=[urlinfo[i]])#线程组
    th1.start()
    thr_list.append(th1)

for i in thr_list:
    i.join()

urlinfo=[]


#用生成器yield生成实现斐波拉切数列
def febir(num):
    x,y=1,1
    f=[x]
    while y < num:
        f.append(y)
        x,y=y,x+y
    else:
        return f
print febir(13)
'''
def is_p(t_int):
    if t_int==1:
        return False
    elif t_int==2:
        return True
    else:
        for i in xrange(2,t_int):
            if  t_int%i==0:
                return False
        return True
def _get(max_num):
    return ([i for i in xrange(1,max_num+1)if is_p(i)])
print _get(101)


