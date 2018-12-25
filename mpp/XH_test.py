# -*- coding:utf-8 -*-
'''
count =1
sum = 0
while (count <= 100):
    sum = sum + count
    count = count + 1
print(sum)
print count



count = 1
sum = 0
while (count <= 100):
    sum = sum + count
    if ( sum > 1000):  #当 sum 大于 1000 的时候退出循环
        break
    count = count + 1
print(sum)


count = 1
sum = 0
while (count <= 100):
    if ( count % 2 == 0):  # 双数时跳过输出
        count = count + 1
        continue
    sum = sum + count
    count = count + 1
print(sum)



for letter in 'Hello 两点水':
    print letter

for i in range(1,6):
    print i


for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print ('%d 是一个合数' % num)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print ('%d 是一个质数' % num)


'''
import pdb
def combine(s1,s2):      # define subroutine combine, which...
    s3 = s1 + s2 + s1    # sandwiches s2 between copies of s1, ...
    s3 = '"' + s3 +'"'   # encloses it in double quotes,...
    return s3            # and returns it.
a = "aaa"
pdb.set_trace()
b = "bbb"
c = "ccc"
final = combine(a,b)
print final
'''
import sys
import  os
import  string
# Cheng
count = 0
while count < 3:
    login = ''
            Hellow welcome to login qqzone!''
    login2 = ''Try again''
    if count == 0:
        print(login)
    else:
        print(login2)
user =input("please input your name:")
passwd = input("please input your password:")
accept = str(user + passwd)
for line in open("C:\\Users\\CH\\Desktop\\file.txt"):
    line = line.strip("\n")
    if accept == line:
        print("Welcome to login QQzone",user)
        exit()
        break
    else:
        continue
print("Your password or username is wrong")
count +=1
if  count == 3:
    print("fuck off")
'''




import re














