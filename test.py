# -*- coding:utf-8 -*-
import urllib2
import cookielib
from collections import Iterable

# filename = 'cookie.txt'
# cookie = cookielib.MozillaCookieJar(filename)
# 创建cookie处理器
#
# reponse = urllib2.urlopen("http://www.baidu.com")
# print reponse.read()


# python参数
# 在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，或者只用其中某些，
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。
def func(a, b, c=0, *args, **kw):
     print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
args = (1,2,3)
kw = {'x':6}
func(*args,**kw)


# # 迭代器，遍历字典dist
# dist = {'a':1,'b':2,'c':3}
# for k,v in dist.iteritems():
#     print k,v
# # 只遍历key（默认就是只遍历key）,迭代结果顺序可能与原dist不一致
# for key in dist:
#     print key
# # 只遍历value
# for value in dist.itervalues():
#     print value
#
# # 判断一个对象是否可迭代，可以导入collections模块的Iterable进行判断from collections import Iterable
# print isinstance('abc',Iterable)
# print isinstance([1,2,3],Iterable)
# print isinstance(123,Iterable)
#
# # 最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数
# # 可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
# for i,value in enumerate([1,2,3]):
#     print i,value

