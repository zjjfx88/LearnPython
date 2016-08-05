# -*- coding:utf-8 -*-
# 求一个数的n次方结果
# 其中n=2为默认参数，如果传参只有一个，则默认n=2，如power（5）


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print power(5, 2)
