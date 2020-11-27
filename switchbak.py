import telnetlib
import re
import codecs
import time
import datetime
import os

now = datetime.datetime.now().strftime('%Y%m%d')
lognow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S ')
path = "./output/%s"%now
if not os.path.exists(path):
    os.makedirs(path)

hostlist = open(r'./switches.txt').readlines()
for host in hostlist:
    try:
        dsthost = host.strip('\n')
        tn = telnetlib.Telnet(dsthost, timeout=15)
#        tn.set_debuglevel(5)
        time.sleep(3)
        tn.write(b'xiaofeng.mao\n')
        time.sleep(1)
        tn.write(b'Password@1234\n')
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
        f = open('%s/%s'%(path,dsthost),'wb')
        f.write(output)
        f.close()
        print (str(lognow+dsthost+' Success'))
    except:
        print (str(lognow+dsthost+' Failed'))
