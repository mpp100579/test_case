#coding=utf-8
#TCP服务器：
from socket import *
from time import ctime

HOST = '192.168.1.220'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print 'waiting for connection...'
    tcpCliSock, addr = tcpSerSock.accept()
    print '...connected from:', addr

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send('[%s] %s' %(ctime(), data))
    tcpCliSock.close()

tcpSerSock.close()

#tcp客户端
from socket import *

HOST = '172.18.36.99' # Server's IP
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send(data)
    data1 = tcpCliSock.recv(BUFSIZ)
    if not data1:
        break
    print data1

tcpCliSock.close()
