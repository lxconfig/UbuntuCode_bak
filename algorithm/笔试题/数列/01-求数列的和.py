
""" 
    数列的定义如下： 数列的第一项为n，以后各项为前一项的平方根，求数列的前m项的和。要求精度保留2位小数
    例：
    81 4   输出：94.73
    2  2   输出：3.41
"""
# import math

# while True:
#     nm = list(map(int, input().split(" ")))
#     n = nm[0]
#     m = nm[1]

#     ret = []

#     for i in range(0, m):
#         ret.append(n)
#         n = math.sqrt(n)
#     print("%.2f" % sum(ret))



# while True:
#     n = int(input())
#     k, i = 3, 3
#     while n - k >= i:
#         i += k
#         k += 1
#     if n < 3:
#         print(n)
#     else:
#         print(n - 2*(k-2))

while True:
    n = int(input())
    sub, k, i = 1, 3, 3
    while n - k >= i:
        k += i
        i += 1
        sub += 1
    if n < 3:
        print(n)
    else:
        print(n - 2*sub)