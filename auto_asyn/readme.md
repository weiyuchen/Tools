# auto_asyn(文件实时同步)
***
#### 预装模块

+ pyinotify

        $ pip3 install pyinotify
#### 本程序块的功能如下：

+ T-pot中的程序：monitor.py以及recv.py，其中monitor.py的主要功能为：
        
        1、监控/data/dionaea/binaries/目录下的文件变化情况
        
        2、对于新增的文件进行上传操作

+ 主机中的程序：sampleBase.py以及send.py，其中sampleBase.py的主要功能为：

        1、在主机中设置服务端接收T-pot中传输过来的样本文件

#### 使用方法：

+ T-pot中：

        $: screen -S monitor        #用screen方式将其运行为守护进程
        $: python3 monitor.py

+ 主机中：

        $: screen -S sample
        $: python3 sampleBase.py

#### 注意事项：

+ 本程序只能在Linux/Unix使用，Windows无法使用
+ 程序中所监控的文件夹等信息可以自由变更
+ 上传的ip,port也可以自己进行调整 
