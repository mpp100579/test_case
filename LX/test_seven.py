#coding=utf-8
import string
#函数isinstance()可以判断一个变量的类型，既可以用在Python内置的数据类型如str、list、dict，也可以用在我们自定义的类，它们本质上都是数据类型。
'''
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

t = Teacher('Alice', 'Female', 'English')

print isinstance(t, Person)
print isinstance(t, Student)
print isinstance(t, Teacher)
print isinstance(t, object)
'''

#自己测试
try:
    class Person(object):
        def __init__(self, nm, ph):
            self.name = nm
            self.phone = ph
        def shout(self):
            return 'his name is %s,phone is%s'%(self.name,self.phone)
    class Kel(Person):
        def __init__(self , age , nm , ph):
            super(Kel,self).__init__(nm,ph)#继承用参数的话：super（本类，self）.__init__(基类paramer1,parameter2)继承基类
            self.age = age
        def test_lambda(self):
            return 'the age is %s'%self.age
    k1 = Kel(18,'mpp1',99999)#单个实例对象
    k2= Kel(19,'MPP2',99998)
    K3= Kel(20,'MPP3',99996)
    k4= Kel(60,'mpp4','678')

finally:
    print k1.shout()

#多个实例对象转换成列表形式,写个txt文件，把实例化对象转成字典（#class的实例都有一个__dict__属性，它就是一个字典，用来存储实例变量。）--再序列化保存test_po.txt文件，序列化后往文件中写,
#import pickle
import json
import string

k_one=k1.__dict__
#print k_one
#k_two=k2.__dict__
#print k_two
#k_t=K3.__dict__
#print k_t
#k_f=k4.__dict__
#print k_f

list_k=[k1.__dict__,k2.__dict__,K3.__dict__,k4.__dict__]#字典转成列表打印
print list_k

file='test_po.txt'
f=open(file,'w')
f.write(json.dumps(k_one))
f.close()

f=open(file,'r')
json_one=json.loads(f.read())
print json_one
f.close()

for i in range(1,n):
    n > = 1000*100
print ' i hope you will be order in %d times'%i

#def dic_one(k1):
    #return {'age':k1.age,'name':k1.name,'phone':k1.phone}

#print(json.dumps(k1,default=dic_one))
#print(json.dumps(k2, default=lambda obj: obj.__dict__))


#pickle.dump(dic,f)  序列化对象









'''
#python中多态
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def whoAmI(self):
        return 'I am a Person, my name is %s' % self.name

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def whoAmI(self):
        return 'I am a Student, my name is %s' % self.name


class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

    def whoAmI(self):
        return 'I am a Teacher, my name is %s' % self.name

import json

class Students(object):
    def read(self):
        return r'["Tim", "Bob", "Alice"]'
s = Students()
print json.load(s)


#除了从一个父类继承外，Python允许从多个父类继承，称为多重继承。Java不能多继承
class A(object):
    def __init__(self, a):
        print 'init A...'
        self.a = a

class B(A):
    def __init__(self, a):
        super(B, self).__init__(a)
        print 'init B...'

class C(A):
    def __init__(self, a):
        super(C, self).__init__(a)
        print 'init C...'

class D(B, C):
    def __init__(self, a):
        super(D, self).__init__(a)
        print 'init D...'
class Person(object):
    pass
class Student(Person):
    pass
class Teacher(Person):
    pass
    
    
class SkillMixin(object):#基类
    pass
    
class BasketballMixin(SkillMixin):
    def skill(self):
        return 'basketball'
class FootballMixin(SkillMixin):
    def skill(self):
        return 'football'

class BStudent(BasketballMixin):
    pass

class FTeacher(FootballMixin):
    pass

s = BStudent()
print s.skill()

t = FTeacher()
print t.skill()

#str=还是觉得看
#开始的发你
#时代峻峰扩扩扩扩扩扩扩扩
#肯定是减肥，

print str
'''