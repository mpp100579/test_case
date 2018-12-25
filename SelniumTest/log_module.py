#coding=utf-8
import time

class Loginfo(object):
    def __init__(self,path='',mode='w'):
        fname=path+time.strftime('%y-%m-%d',time.gmtime())
        self.log=open(path+fname+'.txt',mode)
    def log_write(self,loginfo):
        self.log.write(loginfo)
    def log_close(self):
        self.log.close()


if __name__ =='__main__':
    log=Loginfo()
    log.log_write('test loginfopo 测试')
    log.log_close()
