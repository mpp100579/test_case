#coding=utf-8

password ={'username':'yujian','password':'yujian612'}#创建字典
passwd = open('D:\passwd.txt','r')#以只读的模式打开，确保文件存在否则报错
for n in passwd.readlines(): #读取文件的全部内容
    k = n.split('\t')[0] #以tab为分割取出用户名
    print(k)
    v = n.split('\t')[1]#以tab为分割取出密码
    print (v)
    m = v.split('\n')[0]#以回车为分割符，取出密码的完整内容
    print (m)
    password[k] = m
#如果要看执行效果，就把那几个#去掉
passwd.close()

lock = {}
look = open('D:\socket.txt','r')
for i in look.readlines():
    k1 = i.split('\n')[0]
    lock[k1]=k1
    print (k1)
print (lock)
count = 0
look.close()
username = input("请输入用户名:")
if username in lock.keys():
    print ("该用户已被锁定:")
else:
    pwd = input("请输入密码:")
    if pwd == password[username]:
        print ("登录成功")
    else:
        while count < 2:
            pwd = input("请输入密码:")
            if pwd == password[username]:
                break
            count+=1
        else:
            sok = open("D:\socket.txt",'a+')
            sok.write(username+'\n')
            sok.close()
            print ("登录次数过多，用户被锁定")