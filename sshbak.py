#! /usr/bin/env python3.7
#coding:utf-8

import paramiko
import time
import datetime
import os

#获取当前时间
now = datetime.datetime.now()

#设置输出路径及时间戳
path = "./conf/%s"%now.strftime('%Y%m%d')

#创建目录
if not os.path.exists(path):
    os.makedirs(path)

#读取交换机信息
switches = open(r'./switches.txt').readlines()
for switch in switches:
    try:
        host = switch.split(' ')[0]
        user = switch.split(' ')[1]
        passwd = switch.split(' ')[2].strip('\n')

        #建立ssh连接
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host,username=user,password=passwd)

        #调用shell
        command = ssh.invoke_shell()

        #设置回显内容不分屏
        command.send("sys"+"\n")
        command.send("user-interface vty 0 4"+"\n")
        command.send("screen-length 0"+"\n")
        command.send("quit"+"\n")
        command.send("quit"+"\n")
        
        #获取交换机配置
        command.send("dis cur"+"\n")
        time.sleep(3)

        #输出交换机配置到文件
        output = command.recv(65535)
        file = open('%s/%s'%(path,host+'.cfg'),'wb')
        file.write(output)

        #结束
        file.close()
        ssh.close()

        #输出日志
        print (str(now.strftime('%Y-%m-%d-%H:%M:%S ')+host+' Success'))
    except:
        print (str(now.strftime('%Y-%m-%d %H:%M:%S ')+host+' Failed'))

