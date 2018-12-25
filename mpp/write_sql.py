# -*- coding: utf-8 -*-

__author__ = 'LENOVO'
import MySQLdb
import mysql.connector
import  MySQLdb  as mdb

Conn= MySQLdb.connect(user='wenrui', passwd='wenrui',
                              host='localhost',db='wuliu',charset="utf8") #连接数据库
cur =Conn.cursor()
cur.execute( "CREATE TABLE wuliuData(i VARCHAR(20), l0 VARCHAR(20), t0 VARCHAR(20), L VARCHAR(20), T VARCHAR(20), D VARCHAR(20),F VARCHAR(20),chazhi VARCHAR(20))") #创建表
Conn.commit()

D = [10, 20, 30, 40, 50, 60, 70, 80]
a = 0.5; b = 0.5
#l = 20; t = 5;

def  returnValue(i,l,t,a,b):

     L=a*D[i]+(1-a)*(l+t)
     T=b*(L-l)+(1-b)*t
     F= L+T
     data = (i+2, l, t, L, T, D[i+1], F, F-D[i+1])
     cur.execute("INSERT INTO wuliuData VALUES  (%s, %s, %s, %s, %s, %s, %s, %s)", data)  #将数据写到数据库中
     Conn.commit()

for l in range(1, 26):
    for t in range(1, 26):
        F0=l+t
        data = (1,l,t,"","" ,D[0],F0,l+t-D[0])
        cur.execute("INSERT INTO wuliuData VALUES  (%s, %s, %s, %s, %s, %s, %s, %s)", data)
        for i in range(0, 7):
            returnValue(i,l,t,0.5,0.5)