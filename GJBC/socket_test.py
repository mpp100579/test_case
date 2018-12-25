#coding=utf-8

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',81))
s.listen(8)
while 1:
    connection,address=s.accept()
    buf=connection.recv(10)
    connection.send(buf)
s.close()
