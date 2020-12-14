

"""
    你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
    如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。给定一个代表每个房屋存放金额的非负整数数组，
    计算你不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额
"""


class Solution:
    def rob(self, nums: list) -> int:
        """动态规划
        O(n)  time
        O(n)  space
        """
        if not nums:
            return 0
        n = len(nums)
        yes, no = [0] * n, [0] * n
        yes[0], no[0] = nums[0], 0
        for i in range(1, n):
            yes[i] = nums[i] + no[i-1]
            no[i] = max(no[i-1], yes[i-1])
        return max(yes[-1], no[-1])
    
    def rob_2(self, nums: list) -> int:
        """动态规划-优化
        O(n)  time
        O(1)  space
        """
        if not nums:
            return 0
        yes, no = 0, 0
        for i in nums:
            yes, no = i+no, max(yes, no)
        return max(yes, no)


if __name__ == "__main__":
    s = Solution()
    nums = [2,7,9,3,1]
    print(s.rob(nums))
    