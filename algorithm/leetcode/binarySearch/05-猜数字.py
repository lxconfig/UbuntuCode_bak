

"""
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0

def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        """左区间中位数
        """
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if guess(mid) == 1:
                left = mid + 1
            else:
                right = mid
        return left
    
    def guessNumber_1(self, n: int) -> int:
        """右区间中位数
        """
        left, right = 1, n
        while left < right:
            mid = (left + right + 1) // 2
            if guess(mid) == -1:
                right = mid - 1
            else:
                left = mid
