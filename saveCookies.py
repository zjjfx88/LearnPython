# -*- coding: utf-8 -*-
import urllib2
import cookielib
#使用文件存放cookie
filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
# 创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#创建请求
reponse = opener.open("http://www.baidu.com")
#保存cookies
cookie.save(ignore_discard=True,ignore_expires=True)
file = open('cookie.txt','r')
for line in file.readlines():
    print line
