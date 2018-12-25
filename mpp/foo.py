# -*- coding:utf-8 -*-
import time
import string
import logging
logging.basicConfig(level=logging.INFO)
import FUNC #引入其他模块所有
'''
filename = "foo.py"
def show_filename():
    return "filename: %s" % filename
if __name__ == '__main__':
    print FUNC.use_func(show_filename) #调用执行其他模块的函数

'''
import logging
logging.basicConfig(level=logging.INFO)
def apper():
    alist=range(0,101)
    def lazy_sum(x,y):
        a= reduce(lambda x,y:x+y,alist)
        print a
    return lazy_sum                         #函数作为返回值时候，只需要返回函数名
    logging.warning('you have performed')
if __name__=='__main__':
    sum1 = apper()
    print sum1(3,4)



print string.center('属性封装',90,'*')
d = 100                                  #如果声明d 是全局变量就要先赋值
class Student(object):
    def __init__(self,score,name,age,num):
        self.score=score
        self.__name=name                 #类的属性封装起来用self.__age采用后面的方法暴露属性的获取
        self.__age=age
        self.num=num

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
            print 'B'
        else:
            return 'C'

    def get_name(self,c):           #函数要传参的参数c打印出来，fuc(self,c),如果有其他函数修改本地变量用全局变量吧或者再传个参数作为变量
        global d
        d=d+1
        print 'd is %d'%d
        return 'name is :%s'%self.__name            #类的私有属性self.__name放到方法里，外部获取类的属性通过暴露的方法获取

    def get_age(self):
        return 'age is:%d'%self.__age

    def diao_yong(self):
        return self.get_name(self.num)                     #函数里面调用其他函数方法需要用return self.func(c)&&&&&&&&&&&&&&&&&&&&&&&&&&&

    def getShuxing(self):
        return self.__dict__                               # __dict__变量是个字典，保存的是对象的属性&&&&&&&&&&&&&&&&&&&&&&&&&&&


class SUV(Student):
    def __init__(self,score,name,age,num,sex):
        Student.__init__(self,score,name,age,num)  # 子类调用父类方法也要：父类名.__init__(self,参数1，参数2)

        self.__sex = sex                       #子类自身的私有属性self.__sex和变量sex

    def getShuxing(self,a=[]):                         # 方法同名，子类方法覆盖父类方法,并且传了个列表进来
        Student.getShuxing(self)                      # 调用父类D方法要跟父类一致，类名.func(参数,包含self在内)要用变量接收父类函数的返回值或者直接返回父类.函数(self)的返回值
        a_list=a                                         #列表指给变量a_lsit，其他要调用这个方法时候需要传参进来一个列表并且打印
        print a_list
        return Student.getShuxing(self)
        #return self.__dict__                      # __dict__变量是个字典，保存的是对象的属性&&&&&&&&&&&&&&&&&&&&&&&&&&&

    def get_sex(self):
        #print self.__sex
        return self.__sex

if __name__=='__main__':
    S=Student(77,'dd1',88,200)
    print S.get_grade()
    print S.get_name(900)
    print S.get_age()
    print S.diao_yong()
    print S.getShuxing()
    S2=SUV(66,'GGG',99,200,'man')
    print S2.get_sex()
    print S2.getShuxing([1,3,8,9])