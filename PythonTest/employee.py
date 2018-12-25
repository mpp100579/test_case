#coding=utf-8
class Employee:  #'所有员工的基类'
    empCount = 0
    name=0

    def mppInput(self):
        name = raw_input('please enter your name: ')
        print name
        print 'hello,', name

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
         print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary
        print "分别统计:{0}:{1}".format(self.name , self.salary)

emp1 = Employee("Zara", 2000)  #"创建 Employee 类的第一个对象"
emp2 = Employee("Manni", 5000)  #"创建 Employee 类的第二个对象"
emp1.displayEmployee()
emp2.displayEmployee()
emp1.mppInput()
print "Total Employee %d" % Employee.empCount
print "My name is %s and weight is %d kg!" % ('Zara', 21)

