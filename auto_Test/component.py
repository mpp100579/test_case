# coding:utf8
import string
import sys
import os
import codecs

num=1
equip_name = '风机'
f= open('d:\\component.txt','w+')
for i in range(1,10000):
    num= num + i
    equip_num = bytes(num)

    equip_value =equip_name + equip_num
    equip_key='a11'+equip_num+'='+equip_value
    print (equip_key)

    f.write(equip_key)
    f.write('\n')


#print type(equip_key)
# f = file('d:\\component.txt','w+')
# f.write(equip_key)
'''
p='d:\\component.txt'
def write_txt(txt, path):
    f = codecs.open(p, 'w+', 'utf8')
    f.write(list_equip)
    f.close()
'''

# with open("d:\\component.txt", "w") as f:
    # f.write(equip_key)
