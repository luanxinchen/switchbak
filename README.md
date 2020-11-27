```
╔═╗──╔╦╗──╔╗╔╗───╔╗
║═╬╦╦╬╣╚╦═╣╚╣╚╦═╗║╠╗
╠═║║║║║╔╣═╣║║╬║╬╚╣═╣
╚═╩══╩╩═╩═╩╩╩═╩══╩╩╝
```

#### 交换机配置自动备份脚本
* 基于telnet实现，目前测试支持H3C主流设备
* switches.txt用来存放交换机信息，共IP、账号、密码三列，以空格分隔
* 备份的配置文件根据备份时间存放在`./conf/`目录中
```
[root@it-webpy-master switchbak]# cat switches.txt 
172.16.100.14 xinchen.luan Password@12345
172.16.100.15 xiaofeng.mao Password@1234
[root@it-webpy-master switchbak]# tree conf/
conf/
|-- 20201125
|   |-- 172.16.100.14
|   `-- 172.16.100.15
|-- 20201126
|   |-- 172.16.100.14
|   `-- 172.16.100.15
`-- 20201127
    |-- 172.16.100.14
    `-- 172.16.100.15
```

#### 环境要求
* python3
* telnetlib

#### 脚本执行
使用crontab设置定时任务
```
[root@it-webpy-master switchbak]# crontab -l
#每周一三五的9点30分执行备份
30 9 * * 1,3,5 /usr/bin/python3 /root/switchbak/switchbak.py > /root/switchbak/switchbak.log
[root@it-webpy-master switchbak]# cat switchbak.log 
2020-11-27 18:59:10 172.16.100.14 Success
2020-11-27 18:59:10 172.16.100.15 Success
```

#### todo list
- [x] 多用户多密码支持
- [ ] 多线程支持
- [ ] 自定义命令支持