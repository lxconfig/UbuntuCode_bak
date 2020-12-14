

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, nums: List[int]) -> int:
        """打家劫舍
        自底向上的动态规划
        """
        if not nums: return 0
        size = len(nums)
        dp = [0 for _ in range(size + 1)]
        dp[1] = nums[0]
        for i in range(2, size + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        return dp[size]

    def rob_1(self, nums: List[int]) -> int:
        """打家劫舍
        动态规划-空间优化
        """
        if not nums: return 0
        size = len(nums)
        yes, no = nums[0], 0
        for i in range(1, size):
            yes, no = no + nums[i], max(yes, no)
        return max(yes, no)

    def rob_2(self, nums: List[int]) -> int:
        """打家劫舍
        自顶向下的递归+备忘录
        """
        if not nums: return 0
        size = len(nums)
        memo = dict()
        def dp(i):
            if i == 0: return 0
            if i == 1: return nums[0]
            if i in memo: return memo[i]
            memo[i] = max(dp(i - 1), dp(i - 2) + nums[i - 1])
            # print(memo)
            return memo[i]
        return dp(size)
    
    def rob_3(self, nums: List[int]) -> int:
        """打家劫舍Ⅱ
        """
        if not nums: return 0
        size = len(nums)
        if size == 1: return nums[0]
        ret1 = self.rob_2(nums[0: size - 1])
        ret2 = self.rob_2(nums[1: size])
        return max(ret1, ret2)

    def rob_4(self, root: TreeNode) -> int:
        """打家劫舍Ⅲ
        """
        if not root: return 0
        def dfs(node):
            if not node: return [0, 0]
            left = dfs(node.left)
            right = dfs(node.right)
            print(left, right)
            dp = [0, 0]
            dp[0] = max(left[0], left[1]) + max(right[0], right[1])
            dp[1] = node.val + left[0] + right[0]
            return dp
        res = dfs(root)
        return max(res[0], res[1])


if __name__ == "__main__":
    s = Solution()
    nums = [2,3,2]
    a = TreeNode(3)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(3)
    e = TreeNode(1)
    a.left = b
    a.right = c
    b.right = d
    c.right = e
    print(s.rob_4(a))