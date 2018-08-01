#coding = utf-8
'''
本程序是为了接收样本使用
'''
from send import *
import os

strans = sTrans()

ip = '127.0.0.1'
port = 2000
s = strans.build_socket(ip,port)
s.listen(500)
recvPath = '/home/g6/tmp/'   #接收到的文件可以自定义存放位置

while 1:
    conn,addr = s.accept()
    strans.recving(conn,recvPath)
    strans.close_socket(conn)

