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
for key, group in itertools.groupby('aAabBBcXddDc', lambda c: c.upper()):
    print key, list(group)