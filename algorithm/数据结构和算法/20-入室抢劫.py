
"""
    有一排房子，房子里面都放着一定数额的钱，假设你要去抢钱，怎么才能抢到最多的钱？
    注意：相邻房子的钱只能抢一家

    思路：动态规划，尝试找出一个公式来表示
    如：
    钱数:    9  5  4   7  8  6  3  9  5  2
    抢:      9  5  13  16 ...
    不抢:    0  9  9   13 ...
    以此类推，可以得到两个公式：
    Y(i) = N(i-1) + a[i]
    N(i) = max(Y(i-1), N(i-1))   其中Y(i)表示抢第i个房子最多可以获得的钱数，N(i)表示不抢第i个房子最多可以获得的钱数，a[i]表示第i个房子有的钱数
"""
import pysnooper

# @pysnooper.snoop()
def rob(array):

    # O(n)  time
    # O(n)  space
    # n = len(array)
    # yes = [array[0]] * n
    # no = [0] * n
    # for i in range(1, n):
    #     no[i] = max(yes[i-1], no[i-1])
    #     yes[i] = no[i-1] + array[i]
    # return max(yes[-1], no[-1])
    
    # 优化，减少额外空间
    # O(n)  time
    # O(1)  space
    yes, no = 0, 0
    for i in array:
        no, yes = max(yes, no), no + i   # 最好用赋值表达式，否则不好控制yes和no的值
    return max(yes, no)


def pro_rob(array):
    """房子是环形排列，抢了第一个，最后一个房子也不能抢"""
    # f(1, n) = max(f(1, n-1), f(2, n))  n表示总房数
    # f(1, n)表示要抢1-n号房子
    # f(1, n-1)表示抢了1号房子，那最后的n号房子不能抢，就排除掉
    # f(2, n)表示不抢1号房子，那么可以从2号开始判断抢与不抢
    n = len(array)
    # 抢第一家
    a = helper(array, 0, n-1)

    # 不抢第一家
    b = helper(array, 1, n)
    # print(a, b)
    return max(a, b)
    # return b

# @pysnooper.snoop()
def helper(array, start, end):
    yes, no = array[start], 0
    # print(array[start: end])
    for i in array[start+1: end]:
        no, yes = max(yes, no), no + i
    return max(yes, no)


if __name__ == "__main__":
    # array = [9,5,4,7,8,6,3,9,5,2]
    # array = [2,7,9,3,1]
    array = [4, 1, 1, 9, 1]
    print(rob(array))
    # print(pro_rob(array))