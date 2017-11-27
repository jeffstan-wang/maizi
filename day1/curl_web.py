#!/usr/bin/python
#coding=utf-8
import os
import time
import sys
import pycurl
URL="http://www.baidu.com"
ISOTIMEFORMAT='%Y-%m-%d %X'
c=pycurl.Curl()
c.setopt(pycurl.URL,URL)
c.setopt(pycurl.CONNECTTIMEOUT,5)
c.setopt(pycurl.TIMEOUT,5)
c.setopt(pycurl.FORBID_REUSE,1)
c.setopt(pycurl.MAXREDIRS,1)
c.setopt(pycurl.NOPROGRESS,1)
c.setopt(pycurl.DNS_CACHE_TIMEOUT,30)
indexfile=open(os.path.dirname(os.path.realpath(__file__))+"content.txt","wb")
c.setopt(pycurl.WRITEHEADER,indexfile)
c.setopt(pycurl.WRITEDATA,indexfile)
try:
    c.perform()
except Exception as e:
    print ("content error:" +str(e))
    indexfile.close()
    c.close()
    sys.exit()


NAMELOOKUP_TIME=c.getinfo(c.NAMELOOKUP_TIME)
print(NAMELOOKUP_TIME)