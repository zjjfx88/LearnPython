# -*- coding:utf-8 -*-

# 无限迭代器
import itertools

natuals = itertools.count(1)

#for n in natuals:
#    print n



# cycle()会把传入的一个序列无限重复下去

cs = itertools.cycle('ABC')
#for c in cs:
#    print c

# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
ns = itertools.repeat('A', 10)
#for s in ns:
#    print s


# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
#for c in itertools.chain('abc', 'xyz', '123'):
#    print c


# groupby()把迭代器中*相邻*的重复元素挑出来放在一起：
#for key ,group in itertools.groupby('aaabbbccdddc'):
#    print key, list(group)

# 实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，
# 这两个元素就被认为是在一组的，而函数返回值作为组的key。如果我们要忽略大小写分组，
# 就可以让元素'A'和'a'都返回相同的key：
#for key, group in itertools.groupby('aAabBBcXddDc', lambda c: c.upper()):
#   print key, list(group)


# imap()和map()的区别在于，imap()可以作用于无穷序列，并且，如果两个序列的长度不一致，以短的那个为准。
#for x in itertools.imap(lambda x, y:x*y, [10,20,30],itertools.count(1)):
#    print x

# 注意imap()返回一个迭代对象，而map()返回list。当你调用map()时，已经计算完毕：
#r = map(lambda x:x*x, [1,2,3])
#print r #r应计算出来

# 当你调用imap()时，并没有进行任何计算：
#m = itertools.imap(lambda x:x*x,[4,5,6])
#print m
# <itertools.imap object at 0x103d3ff90> 输出是个迭代对象
# 需要循环遍历才能取出
#for i in m:
#    print i

r = itertools.imap(lambda x:x*x, itertools.count(1))
for n in itertools.takewhile(lambda x:x<100,r):
    print n

# ifilter() ifilter()就是filter()的惰性实现。