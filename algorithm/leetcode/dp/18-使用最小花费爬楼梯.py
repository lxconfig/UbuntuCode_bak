

"""
    数组的每个索引作为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
    每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
    您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。
"""
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost: return 0
        size = len(cost)
        dp = [0 for _ in range(size)]
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, size):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(dp[-1], dp[-2])

    def minCostClimbingStairs_1(self, cost: List[int]) -> int:
        """空间优化
        """
        if not cost: return 0
        size = len(cost)
        dp_1, dp_2 = 0, 0
        for i in range(size):
            dp_1, dp_2 = min(dp_1, dp_2) + cost[i], dp_1
        return min(dp_1, dp_2)


if __name__ == "__main__":
    s = Solution()
    cost = [10, 15, 20]
    print(s.minCostClimbingStairs_1(cost))