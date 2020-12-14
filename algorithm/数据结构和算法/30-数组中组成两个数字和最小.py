

"""
    给定一个数组，从中组合出两个数字，要求这两个数字之和最小，并且数组中每个数字都要用到

    思路：用最小堆，把元素分开，组合成数字（每次取出来的都是当前数组中的最小值）
    num = num * 10   用来计算两位数三位数四位数.....
"""

import heapq



def minSum(array):
    heapq.heapify(array)   # 构成最小堆
    num1 = 0
    num2 = 0
    while array:
        num1 = num1 * 10 + heapq.heappop(array)
        if array:
            # 这个判断是因为当数组个数是奇数时，执行上面num1的语句后，array就已经为空。不能在执行下去
            # 所以要增加判断
            num2 = num2 * 10 + heapq.heappop(array)
        
    return num1 + num2


if __name__ == "__main__":
    array = [5, 3, 0, 7, 4]
    print(minSum(array))
