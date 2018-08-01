#coding=utf-8
import os
import socket
import struct

class cTrans():
    def start_socket(self,ip,port):
        #set up the socket and try to connect
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,port))
        #conn = s.accept()
        return s

    def pulling(self,socket):
        s = socket
        # s = section
        recv_info = struct.calcsize('128sl')
        buf = s.recv(recv_info)
        recv_name = ''
        if buf:
            recv_name,recv_size = struct.unpack('128sl',buf)
            # recv_name = recv_name.strip
            #print(str(recv_name, encoding='utf8'))
            newFileName = bytes.decode(recv_name).rstrip('\x00')
            # recv_name = os.path.join('./'+'new_'+newFileName)
            recv_name = os.path.join('./tmp_result/'+newFileName)

            recvd_size = 0
            recv_handle = open(recv_name,'wb')
            # print('starting receiving...')

            while not recvd_size == recv_size:
                if recv_size - recvd_size >1024:
                    recv_data = s.recv(1024)
                    recvd_size += len(recv_data)
                else:
                    recv_data = s.recv(recv_size - recvd_size)
                    recvd_size = recv_size
                recv_handle.write(recv_data)
            recv_handle.close()
            # print('receiving finished!')
        return recv_name

    def pushing(self,socket,file_path):
        s = socket
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

    def stop_socket(self,socket):
        s = socket
        # conn = connection
        s.close()

# #init the cTrans()
# ctrans = cTrans()

# s = ctrans.start_socket()
# # conn,addr = s.accept()
# ctrans.pulling(s)

# filePath = input("please input a file path:")
# ctrans.pushing(s, filePath)
# ctrans.stop_socket(s)
