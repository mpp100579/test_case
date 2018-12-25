#coding=utf-8
import time
import os

'''
source=[r'E:\python\app.doc']
target_dir='E:\mpp'
target=target_dir+time.strftime('%Y%m%d%H%M%S')+'.zip'
zip_command="zip-qr'%s'%s"%(target,''.join(source))

if os.system(zip_command)==0:
    print 'successful backup to',target
else:
    print 'BACKUP FAILED'

print time.strftime('%Y%m%d%H%M%S')#打印当前时间
today = target_dir + time.strftime('%Y%m%d')


#类方法

class TestMethod(object):
    def foo(self, x):  # 定义类中的普通函数，传递参数为self，也就是类的实例
        print 'excuting foo(%s,%s)' % (self, x)

    @staticmethod  # 定义静态方法，在其中不传递参数
    def static_foo(x):
        print 'excuting static_foo(%s)' % x

    @classmethod  # 传递类方法，在其中传递的参数为cls
    def class_foo(cls, x):
        print 'excuting class_foo(%s,%s)' % (cls, x)

kel = TestMethod()
kel.foo(1)
kel.static_foo(1)
kel.class_foo(1)
TestMethod.static_foo(1)
TestMethod.class_foo(1)

print (kel.foo)
print (kel.static_foo)
print (kel.class_foo)



class Kel(object): #父类方法
    def __init__(self):
        print 'Kel class called'
class J(Kel):#J是继承Kel类
    def __init__(self): #重写了init方法
        print 'J class is called'
class M(Kel):#M继承Kel类
    def __init__(self):#重写了init方法
        super(M,self).__init__()#调用了父类的方法，调用父类初始化
        print 'M class is called'
print '-'*10
kel = Kel()
print '-'*10
j = J()
print '-'*10
m = M()
可以看到，如果子类写了自己的init方法，那么不会自动的调用父类的init方法，必须在子类的init方法中自己进行调用，如上子类M所示
每个子类最好构造自己的构造器，不然积累的构造器会被调用，然而，如果子类重写基类的构造器，基类的构造器就不会被自动调用了。
a、 基类的构造器就必须显式的写出来才会被执行
b、 传递self的实例对象给基类进行调用，在上面的例子中，使用的是内建方法super，最好是使用super方法
在使用super调用基类方法的时候，找到基类方法，并且传入self参数即可，不需要明确指定父类的名字，并且在修改的时候，也是容易修改的。


class Phone1(object):
    def __init__(self, ph1):
        self.phone = ph1
class Person(object):
    def __init__(self, nm, ph2):
        self.name = nm
        self.phone = Phone1(ph2)

p = Person('kel', '1234143')
print 'his name is %s,phone is%s'%(p.name,p.phone.phone)
如上代码所示，使用的是组合的方式，在类Phone中，表示手机号码，而在类Person中包含了一个phone对象，那么就表示person has-a phone，
类与类之间的关系为has-a的关系，在一个类中包含其他类的实例，就表示为组合。

'''

try:
    class Person(object):
        def __init__(self, nm, ph):
            self.name = nm
            self.phone = ph
        def shout(self):
            return self.name
    class Kel(Person):
        def __init__(self , age , nm , ph):
            Person.__init__(self, nm, ph) #方法2调用父类初始化
            #super(Kel ,self).__init__(nm,ph)  #方法1调用父类初始化
            self.age = age
    k = Kel(12, 'DJFSK',8888)
    print 'age is %d,nm is %s,ph is%d'%(k.age,k.nm,k.ph)
except NameError:
    k = Kel(12, 'DJFSK', 8888)
    print '对象不存在'
finally:
    print 'age is %d'%k.age




#如上的代码中Kel继承了person类，从而表示为类与类之间的关系为派生关系，也就是表示：相同的类具有一些不同的功能，从而可以写出自己的方法。一个子类可以继承它的基类的任何属性，不关是数据属性还是方法。在继承中可以覆盖父类的方法，——直接使用同名的函数即可进行覆盖，也就是所谓的override方法'''
'''
class People(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
class Teacher(People):
    def __init__(self, name, gender, course):
        super(People, self).__init__(name, gender)          #调用父类初始化
        self.course = course
t = Teacher('Alice', 'Female', 'English')
print t.name
print t.course
'''