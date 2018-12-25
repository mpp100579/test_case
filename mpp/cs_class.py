#coding=utf-8
import pickle

#print help(pickle)


__all__ = ['getInfo']


class Car:
     #wheelNumber = 4    # 公有属性，跟java不同的是，属性在__init__方法中声明即可
     #color = 'yellow'
     #material='oil'
     #__type = 'SUV1'     # 私有属性,__也是属性名的一部分

    def __init__(self, wheelNumber, color, type):  # 构造函数，self相当于java中的this
        self.__wheelNumber = wheelNumber  # 类的成员变量在构造函数中定义，并且是私有的
        self.__color = color
        self.__type = type


    def getInfo(self,a=[]):  # 类中的方法都要有self，类外调用则不要传self参数
        a_list=[1,3,5]
        print('我有%d个轮子的%s，颜色是：%s' % (self.__wheelNumber, self.__type, self.__color))
        #return a_list
        return self.__dict__  # __dict__变量是个字典，保存的是对象的属性&&&&&&&&&&&&&&&&&&&&&&&&&&&

    def getType(self):
        return self.__type



    def getShuxing(self):#this，self表示使用本类的,就类似初始化,类下面的函数都要带有self
        return self.__dict__  # __dict__变量是个字典，保存的是对象的属性


if __name__ == '__main__':
    car1 = Car(2, 'blue', 'Bike')
    car1.getInfo()  # 对象访问方法
    # print(car1.__type)   #  对象访问私有属性会报错,一般不直接访问属性
    print(car1.getType())  # 用get属性方法访问属性
    print(car1.getShuxing())


class SUV(Car):  # 类名后面的小括号表示继承
    def __init__(self, wheelNumber, color, type, qudong):
        Car.__init__(self, wheelNumber, color, type)  # 调用父类方法也要父类名.__init__(self,参数1，参数2)

        self.__qudong = qudong                        #子类自身的属性和变量qudong

    def getInfo(self):                         # 方法同名，子类方法覆盖父类方法
        Car.getInfo(self,a=[])                      # 调用父类方法要跟父类一致，类名.func(参数,包含self在内)
        a_list=[2,4,6,8]
        print a_list
        print('我是%d驱的' % (self.__qudong))

    def run(self):
        print(self.getType())

    def getShuxing(self):
        return self.__dict__


if __name__ == '__main__':
    car2 = SUV(4, 'red', 'SUV', 2)
    car2.getInfo()
    car2.getType()
    print(car2.getShuxing())