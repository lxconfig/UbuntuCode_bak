

"""
    实现int(sqrt(x))的功能
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        # 一个数的平方根一定不会超过它本身
        # 一个数的平方根最多不会超过它的一半
        # (a // 2) ^ 2 >= a
        if x == 0: return 0
        left, right = 0, x // 2 + 1
        while left < right:
            # 取右区间中位数
            mid = (left + right + 1) // 2
            square = mid * mid
            if square > x:
                right = mid - 1
            else:
                left = mid 
        return left

    def mySqrt_1(self, x: int) -> int:
        if x == 0: return 0
        left, right = 0, x // 2 + 1
        while left < right:
            # 取左区间中位数
            mid = (left + right) // 2
            print(left, right, mid)
            square = mid * mid
            if square < x:
                left = mid + 1
            else:
                right = mid
        return right


if __name__ == "__main__":
    s = Solution()
    x = 8
    print(s.mySqrt(x))