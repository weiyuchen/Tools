#coding = utf-8
'''
本程序的目的是为了对于文件夹做监控，如果目录有变化就进行上传
'''

import pyinotify
import threading
from recv import *

wm = pyinotify.WatchManager()
ctrans = cTrans()
mask = pyinotify.IN_CREATE | pyinotify.IN_MODIFY

#需要上传的ip和port信息设置
ip = '127.0.0.1' 
port = 2000

def sending(ip,port,filePath):
    s =  ctrans.start_socket(ip,port)
    ctrans.pushing(s,filePath)
    ctrans.stop_socket(s)


class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self,event):
        #sending(ip,port,event.pathname)  #所有的新增文件均上传
        #对于新增的文件进行上传的操作
        if 'tmp' not in event.pathname:     #对于某些文件做过滤
            sending(ip,port,event.pathname)

    def process_IN_MODIFY(self,event):
        if 'tmp' not in event.pathname:
            sending(ip,port,event.pathname)

handler = EventHandler()
notifier = pyinotify.Notifier(wm,handler)
wdd = wm.add_watch('/data/dionaea/binaries/',mask,rec = True)   #所监控的文件夹可以自定义
notifier.loop()




