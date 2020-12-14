

"""
    一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

    假设在初始时青蛙在第n层，就有n-1种跳法，即: f(n) = f(n-1) + f(n-2) + ... + f(1)
    若青蛙在第n-1层，就有n-2种跳法，即: f(n-1) = f(n-2) + f(n-3) + ... + f(1)
    所以: f(n) = 2f(n-1)

    运行时间：22ms
    占用内存：5736k
"""


class Solution:
    def jumpFloorII(self, number):
        if number < 1:
            return 0
        elif number == 1:
            return 1
        else:
            # a表示上一次的结果，ret表示本次的结果
            a, ret = 1, 1
            for _ in range(2, number+1):
                ret = 2 * a
                a = ret
            return ret




if __name__ == "__main__":
    solution = Solution()
    print(solution.jumpFloorII(5))

