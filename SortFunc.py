# -*- coding:utf-8 -*-
# Python内置的sorted()函数就可以对list进行排序：
l = [32, 1, 4, 6, 100]
print sorted(l)

# sorted()函数也是一个高阶函数，它还可以接收一个比较函数来实现自定义的排序。比如，如果要倒序排序，
# 我们就可以自定义一个reversed_cmp函数：


def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0

print sorted(l, reversed_cmp)


# 字符串排序
strList = ['bob', 'about', 'Zoo', 'Credit']
print sorted(strList)
# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
# 所以默认结果是['Credit', 'Zoo', 'about', 'bob']
# 需要添加方法，进行处理，比如全部变成大写或者小写，然后再进行排序


def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0

print sorted(strList, cmp_ignore_case)

# 先做排序，从小到大，然后位移为-1，从最后一个开始取
print sorted([36, 5, 12, 9, 21])[::-1]

print [1,2,3,4][::-1]