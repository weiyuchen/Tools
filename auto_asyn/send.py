
#coding=utf-8
import os
import socket
import struct

class sTrans():
    def build_socket(self,ip,port):

        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((ip,port))
        return s

    def sending(self,file_path,socket):
        s = socket
        #sending chosen file
        if os.path.isfile(file_path):
            file_info = struct.calcsize('128sl')#pack the file
            #define the file head,including file name and size
            file_head = struct.pack('128sl',bytes(os.path.basename(file_path), encoding='utf8'),os.stat(file_path).st_size)
            s.send(file_head)
            #because 'with...as...' has trouble in sending,we choose open()
            file_handle = open(file_path,'rb')
            while True:
                file_content = file_handle.read(1024)
                if not file_content:
                    break
                s.send(file_content)
            file_handle.close()
            # print('sending finished!')
     
    def recving(self,connection,recvPath):
        conn = connection
        #s = socket
        #conn,addr = s.accept()
        recv_info = struct.calcsize('128sl')
        buf = conn.recv(recv_info)
        if buf:
            recv_name,recv_size = struct.unpack('128sl',buf)
            # recv_name = recv_name.strip
            # print(str(recv_name, encoding='utf8'))
            newFileName = bytes.decode(recv_name).rstrip('\x00')
            recv_name = recvPath + newFileName
            recvd_size = 0
            recv_handle = open(recv_name,'wb')

            while not recvd_size == recv_size:
                if recv_size - recvd_size >1024:
                    recv_data = conn.recv(1024)
                    recvd_size += len(recv_data)
                else:
                    recv_data = conn.recv(recv_size - recvd_size)
                    recvd_size = recv_size
                recv_handle.write(recv_data)
            recv_handle.close()
            return recv_name

    def close_socket(self,connection):
        conn = connection
        conn.close()
