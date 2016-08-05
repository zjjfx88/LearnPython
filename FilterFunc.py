# -*- coding:utf-8 -*-

# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的时，filter()把传入的函数依次作用于每个元素
# 然后根据返回值是True还是False决定保留还是丢弃该元素。

# 取奇数


def is_odd(n):
    return n % 2 == 1

print filter(is_odd, [1, 2, 6, 9, 5, 18, 15])
