

"""
    给定一个无序的整数数组，找到其中最长上升子序列的长度。
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """动态规划
        O(n^2)  time
        """
        if not nums: return 0
        size = len(nums)
        dp = [1] * size

        for i in range(size):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def lengthOfLIS_1(self, nums: List[int]) -> int:
        """
            耐心排序(就是蜘蛛纸牌的玩法)
        """
        if not nums: return 0
        size = len(nums)
        top, piles = [0] * size, 0
        for i in range(size):
            poker = nums[i]
            left, right = 0, piles
            while left < right:
                mid = (left + right) // 2
                if top[mid] > poker:
                    right = mid
                elif top[mid] < poker:
                    left = mid + 1
                else:
                    right = mid
            if left == piles:
                piles += 1
            top[left] = poker
        return piles



if __name__ == "__main__":
    s = Solution()
    nums = [10,9,2,5,3,7,101,18]
    print(s.lengthOfLIS_1(nums))