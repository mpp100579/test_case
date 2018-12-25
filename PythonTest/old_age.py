#!/usr/bin/env python
# -*- coding: utf-8 -*-


my_age = 28

user_input = int(input("input your guess num1:"))

if user_input == my_age:
    print("Congratulations, you got it !")
elif user_input > my_age:
    print("Oops,think bigger!")
else:
    print("think smaller!")


count = 0
while count < 3:
    user_input = int(input("input your guess num2:"))

    if user_input == my_age:
        print("Congratulations, you got it !")
        break
    elif user_input < my_age:
        print("Oops,think bigger!")
    else:
        print("think smaller!")
    count += 1  # 每次loop 计数器+1
else:
    print("猜这么多次都不对,你个笨蛋.")