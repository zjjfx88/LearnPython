# -*- coding:utf-8 -*-
#读取存放在文件中的cookie并使用

import urllib2
import cookielib

#创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookie.load('cookie.txt',ignore_expires=True,ignore_discard=True)
#创建请求的request
req = urllib2.Request("http://www.baidu.com")
#利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
reponse = opener.open(req)

print reponse.read()