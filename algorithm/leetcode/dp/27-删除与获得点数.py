
"""
"""

from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums: return 0
        count = [0 for _ in range(max(nums) + 1)]
        size = len(count)
        for i in nums:
            count[i] += 1
        dp = [0 for i in range(size)]
        dp[0], dp[1] = 0, count[1]
        for i in range(2, size):
            dp[i] = max(dp[i - 1], dp[i - 2] + count[i] * i)
        print(dp)
        return dp[-1]



if __name__ == "__main__":
    s = Solution()
    nums = [2, 2, 3, 3, 3, 4]
    print(s.deleteAndEarn(nums))