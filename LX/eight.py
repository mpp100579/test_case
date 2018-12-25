#coding=utf-8
import random

'''
s = random.randint(1,10)
temp=input('请输入一个数字：')
guess=int(temp)
if guess==s:
    print '猜对了，恭喜'
count = 1                       #遍历循环次数用，count=1开始统计

while guess!=s:
    temp=input('输错了，重新输入:')
    guess = int(temp)
    if guess == s:
        print '猜对了，恭喜'
    else:
        if guess > s:
            print 'too large'
        else:
            print 'too small'
    count+=1
    if count==5:
        print 'no change'
print 'game over'
'''
                       #用enumerate(s)遍历字符串列表打印统计元素数目
s = ['abc', 'This is a test', 'Hello, Python']
for i, line in enumerate(s):
    print i+1, line



#把1+。。。100打印出来，方法一：
s=sum([ x for x in range(0,101)])
print s
#方法二：
n = 0
for x in range(101):
   n = x + n
print n


#把1--100的基数打印出来
#s1=sum[x for x in range(1,101) if x%2==0]
#print s1
print(sum(range(1,100,2)))
#方法二：
sum = 0
'''for i in range(1,100,2):
    sum = sum +i
    print sum
'''
for i in range(0,100,2):
    sum = sum +i
    print sum

#闭包:函数是一个对象，所以可以作为某个函数的返回结果。
def line_conf():
    def line(x):
        return 2*x+1
    return line       # return a function object
my_line = line_conf()
print my_line(5)




print '--' * 30  # 划横线的长度
class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary