# -*- coding:utf-8 -*-
#coding=utf-8


import numpy as np
import pandas as pd

df = pd.DataFrame(pd.read_csv('tests.csv',header=1))
df = pd.DataFrame(pd.read_excel(r'E:\python2.7.9\python_test\test_case\pandas\new.xlsx'))

df = pd.DataFrame({"id":[1001,1002,1003,1004,1005,1006],
 "date":pd.date_range('20130102', periods=6),
  "city":['Beijing ', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
 "age":[23,44,54,32,34,32],
 "category":['100-A','100-B','110-A','110-C','210-A','130-F'],
  "price":[1200,np.nan,2133,5433,np.nan,4432]},
  columns =['id','date','city','category','age','price'])
print df.shape
print df.info()


'''
import xlrd

data = xlrd.open_workbook('新建 XLS 工作表.xls',encoding_override='gbk')
print table.row_values(2)
'''