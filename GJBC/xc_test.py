#coding=utf-8

import threading
import time
'''
exitFlag = 0
class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print "Starting " + self.name
        print_time(self.name, self.counter, 5)
        print "Exiting " + self.name


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            (threading.Thread).exit()
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1


# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启线程
thread1.start()
thread2.start()

print "Exiting Main Thread"
'''


import threading
import time

'''start是启动线程，join是阻塞当前线程，即使得在当前线程结束时，不会退出。从结果可以看到，主线程直到Thread-1结束之后才结束。
Python中，默认情况下，如果不加join语句，那么主线程不会等到当前线程结束才结束，但却不会立即杀死该线程。如不加join输出如下：'''

def target():
    print 'the curent threading  %s is running' % threading.current_thread().name
    time.sleep(1)
    print 'the curent threading  %s is ended' % threading.current_thread().name

print 'the curent threading  %s is running' % threading.current_thread().name
t = threading.Thread(target=target)

t.start()
t.join()
print 'the curent threading  %s is ended' % threading.current_thread().name

'''但如果为线程实例添加t.setDaemon(True)之后，如果不加join语句，那么当主线程结束之后，会杀死子线程。代码：'''
def target():
    print 'the curent threading  %s is running' % threading.current_thread().name
    time.sleep(4)
    print 'the curent threading  %s is ended' % threading.current_thread().name
print 'the curent threading  %s is running' % threading.current_thread().name
t = threading.Thread(target=target)
t.setDaemon(True)
t.start()
t.join()
print 'the curent threading  %s is ended' % threading.current_thread().name

'''如果加上join,并设置等待时间，就会等待线程一段时间再退出：'''
def target():
    print 'the curent threading  %s is running' % threading.current_thread().name
    time.sleep(4)
    print 'the curent threading  %s is ended' % threading.current_thread().name
print 'the curent threading  %s is running' % threading.current_thread().name
t = threading.Thread(target=target)
t.setDaemon(True)
t.start()
t.join(1)




