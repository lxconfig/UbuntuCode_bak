"""
    给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

    保证base和exponent不同时为0

    运行时间：22ms
    占用内存：5732k
"""


import math

class Solution:
    def Power(self, base, exponent):
        # write code here
        '''
        if exponent == 0:
            return float(1)
        elif base == 0:
            return 0
        else:
            return math.pow(base, exponent)
        '''
        
        ret = 1
        if base == 0:
            return 0
        if exponent == 0:
            return float(1)
        if exponent < 0:
            for _ in range(-exponent):
                ret *= base
            return 1/ret
        for _ in range(exponent):
            ret *= base
        return ret
