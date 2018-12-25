# -*- coding:utf-8 -*-


#设计一个函数，在桌面创建10个文本，用数字从1-10依次给它们命名。
def text_create():
    path = 'C:\Users\Administrator\Desktop'
    for text_name in range(1,11):
        # 1-10的范围需要用到range函数
        with open (path + str(text_name) + '.txt','w') as text:
            # with...as的用法正文内会详细介绍
            text.write(str(text_name))
            text.close()
            print('Done')
text_create()



#执行语句可以是单个语句或语句块
count = 0
while (count < 9):
    print 'The count is:', count
    count = count + 1
print "Good bye!"




'''while 语句时还有另外两个重要的命令 continue，break 来跳过循环，continue 用于跳过该次循环，break 则是用于退出循环，此外"判断条件"还可以是个常值，表示循环必定成立，具体用法如下：'''
# continue 和 break 用法
i = 1
while i < 10:
    i += 1
    if i % 2 > 0:  # 非双数时跳过输出
        continue
    print i  # 输出双数2、4、6、8、10

i = 1
while 1:  # 循环条件为1必定成立
    print i  # 输出1~10
    i += 1
    if i > 10:  # 当i大于10时跳出循环
        break




#无限循环whiele param=
var = 1
while var == 1:  # 该条件永远为true，循环将无限执行下去
    num = raw_input("Enter a number  :")
    print "You entered: ", num
    break
print "Good bye!"