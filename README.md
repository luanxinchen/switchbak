```
╔═╗──╔╦╗──╔╗╔╗───╔╗
║═╬╦╦╬╣╚╦═╣╚╣╚╦═╗║╠╗
╠═║║║║║╔╣═╣║║╬║╬╚╣═╣
╚═╩══╩╩═╩═╩╩╩═╩══╩╩╝
```

#### 交换机配置自动备份脚本



- 目前测试支持H3C主流设备，其他品牌需要自定义命令
- `sshbak.py` 基于ssh协议实现，适用于绝大部分设备（相较于telnet协议更加安全，推荐）
- `telbak.py` 基于telnet实现，用于某些原因不支持ssh的设备（传输过程没有加密，不推荐）
- `switches.txt` 用来存放交换机信息，分为`IP、账号、密码`三列，以空格符分隔
- `conf`目录用于存放输出的配置文件
```
[root@it-webpy-master switchbak]# cat switches.txt 
172.16.100.14 username password
172.16.100.15 username password
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
* paramiko

#### 脚本执行

##### sshbak.py

```shell
#安装paramiko依赖
[root@it-webpy-master switchbak]# pip3 install paramiko

#Python3执行
[root@it-webpy-master switchbak]# python3 sshbak.py
2021-07-30 15:36:56 172.16.100.14 Failed
2021-07-30 15:36:56 172.16.100.15 Success
```

##### telbak.py

```shell
#python2/3执行
[root@it-webpy-master switchbak]# python telbak.py
2021-07-30 15:36:56 172.16.100.14 Failed
2021-07-30 15:36:56 172.16.100.15 Success
```

##### 设置crontab定时备份

```shell
[root@it-webpy-master switchbak]# crontab -l
#每周一三五的9点30分执行备份
30 9 * * 1,3,5 /usr/bin/python3 /root/sshbak/sshbak.py > /root/switchbak/bakup.log
[root@it-webpy-master switchbak]# cat switchbak.log 
2020-11-27 18:59:10 172.16.100.14 Success
2020-11-27 18:59:10 172.16.100.15 Success
```

#### Todo

- [x] ssh协议支持

- [x] 多用户多密码支持
- [ ] 交换机信息存储加密
- [ ] 多线程支持
- [ ] 自定义命令支持