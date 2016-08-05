# -*- coding:utf-8 -*-
# map方法,接收一个函数和一个序列
# 每次取13579中的一个，进入方法char2num，相当于取return中对应索引的值
# reduce方法,接收一个函数和一个序列
# reduce调用的方法至少两个入参，将结果与序列中的下一个元素继续累计处理


def str2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def add(x, y):
    return x*10 + y

print reduce(add, map(str2num, '13579'))
