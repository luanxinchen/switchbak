#!/usr/bin/env python
#coding:utf-8

import telnetlib
import re
import codecs
import time
import datetime
import os

#获取当前时间
now = datetime.datetime.now()

#设置输出路径及时间戳格式
path = "./conf/%s"%now.strftime('%Y%m%d')

#创建目录
if not os.path.exists(path):
    os.makedirs(path)

#读取交换机信息
contents = open(r'./switches.txt').readlines()
for content in contents:
    try:
        host = content.split(' ')[0]
        user = content.split(' ')[1]
        passwd = content.split(' ')[2]
        
        #建立telnet连接
        tn = telnetlib.Telnet(host, timeout=15)
        #tn.set_debuglevel(5)
        time.sleep(3)
        tn.write(user.encode('ascii') +b'\n')
        time.sleep(1)
        tn.write(passwd.encode('ascii'))
        time.sleep(1)

        #执行命令
        tn.write(b'sys\n')
        tn.write(b'user-interface vty 0 4\n')
        tn.write(b'screen-length 0\n')
        tn.write(b'quit\n')
        tn.write(b'quit\n')
        time.sleep(3)
        tn.write(b'dis cur\n')
        tn.write(b'quit\n')

        #获取输出内容到文件
        output = tn.read_all()
        f = open('%s/%s'%(path,host+'.cfg'),'wb')
        f.write(output)

        #结束
        f.close()
        tn.close()

        #输出日志
        print (str(now.strftime('%Y-%m-%d %H:%M:%S ')+host+' Success'))
    except:
        print (str(now.strftime('%Y-%m-%d %H:%M:%S ')+host+' Failed'))
