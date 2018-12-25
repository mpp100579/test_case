#coding=utf-8
'''
from url import get_page#从当前同级模块引入方法
from url import *#从当前同级模块引入*
import url#从当前同级模块直接引入模块
#import sys
#sys.path.append('LX/test_case')
#print sys.path#查看sys模块的路径


#print get_paper()





from cs_class import Car
from cs_class import SUV

print get_page()
print url.get_page()
print url.get_window()

xc=Car(3,'white','md')
print xc.getInfo()
print xc.getShuxing()
print xc.getType()
print dir(url)#查看下该模块下或者该类下有哪些方法
print dir(Car)#查看下该模块下或者该类下有哪些方法

one=SUV(4,'red','mpp',5,)
print one.getInfo()
print one.getType()
print one.getShuxing()




from time import ctime,sleep

def music():
    for i in range(2):
        print "I was listening to music. %s" %ctime()
        sleep(1)

def move():
    for i in range(2):
        print "I was at the movies! %s" %ctime()
        sleep(5)

if __name__ == '__main__':
    music()
    move()
    print "all over %s" %ctime()
'''

#https://www.cnblogs.com/yeayee/p/4952022.html

import threading
from time import ctime,sleep


def music(func):
    for i in range(2):
        print "I was listening to %s. %s" %(func,ctime())
        sleep(1)

def move(func):
    for i in range(2):
        print "I was at the %s! %s" %(func,ctime())
        sleep(5)
#创建了threads数组，创建线程t1,使用threading.Thread()方法，在这个方法中调用music方法target=music，args方法对music进行传参。 把创建好的线程t1装到threads数组中。接着以同样的方式创建线程t2，并把t2也装到threads数组。
threads = []
t1 = threading.Thread(target=music,args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=move,args=(u'阿凡达',))
threads.append(t2)

if __name__ == '__main__':#最后通过for循环遍历数组。（数组被装载了t1和t2两个线程）
    for t in threads:
        t.setDaemon(True)  #　setDaemon(True)将线程声明为守护线程，必须在start() 方法调用之前设置，如果不设置为守护线程程序会被无限挂起。子线程启动后，父线程也继续执行下去，当父线程执行完最后一条语句print "all over %s" %ctime()后，没有等待子线程，直接就退出了，同时子线程也一同结束。
        t.start()
    t.join()#join（）的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞。join()方法的位置是在for循环外的，也就是说必须等待for循环里的两个进程都结束后，才去执行主进程。
    print "all over %s" %ctime()


