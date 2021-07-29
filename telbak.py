#!/usr/bin/env python
#coding:utf-8
import telnetlib
import re
import codecs
import time
import datetime
import os

now = datetime.datetime.now()
path = "/mnt/nas/switches/%s"%now.strftime('%Y%m%d')
if not os.path.exists(path):
    os.makedirs(path)

contents = open(r'./switches.txt').readlines()
for content in contents:
    try:
        host = content.split(' ')[0]
        user = content.split(' ')[1]
        passwd = content.split(' ')[2]
        tn = telnetlib.Telnet(host, timeout=15)
        #tn.set_debuglevel(5)
        time.sleep(3)
        tn.write(user.encode('ascii') +b'\n')
        time.sleep(1)
        tn.write(passwd.encode('ascii'))
        time.sleep(1)
        tn.write(b'sys\n')
        tn.write(b'user-interface vty 0 4\n')
        tn.write(b'screen-length 0\n')
        tn.write(b'quit\n')
        tn.write(b'quit\n')
        time.sleep(3)
        tn.write(b'dis cur\n')
        tn.write(b'quit\n')
        output = tn.read_all()
        f = open('%s/%s'%(path,host),'wb')
        f.write(output)
        f.close()
        print (str(now.strftime('%Y-%m-%d %H:%M:%S ')+host+' Success'))
    except:
        print (str(now.strftime('%Y-%m-%d %H:%M:%S ')+host+' Failed'))
