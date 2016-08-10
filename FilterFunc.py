# -*- coding:utf-8 -*-

# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的时，filter()把传入的函数依次作用于每个元素
# 然后根据返回值是True还是False决定保留还是丢弃该元素。

# 取奇数
# filter(function or None, sequence) -> list, tuple, or string
# function是一个谓词函数，接受一个参数，返回布尔值True或False。
# filter函数会对序列参数sequence中的每个元素调用function函数，最后返回的结果包含调用结果为True的元素。
# 返回值的类型和参数sequence的类型相同

def is_odd(n):
    return n % 2 == 1

print filter(is_odd, [1, 2, 6, 9, 5, 18, 15])
