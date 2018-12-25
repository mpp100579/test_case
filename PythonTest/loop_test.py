# _*_coding:utf-8_*_
count = 0 #计算器计数,count 初始化为0；
while True:
    print("你是风儿我是沙,缠缠绵绵到天涯...")
    count += 1 #每次计数器加1
    if count == 6:
        print("去你妈的风和沙,你们这些脱了裤子是人,穿上裤子是鬼的臭男人..")
        break

i = 0
for i in range(10):
    if i<5:
        continue #不往下走了,直接进入下一次loop
    print("loop:", i )

