

"""
    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
"""
# import pysnooper


class Solution:
    # @pysnooper.snoop()
    def maxSubArray(self, nums: list) -> int:
        if not nums: return 0
        n = len(nums)
        dp = [float("-inf")] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)

    def maxSubArray_1(self, nums: list) -> int:
        """区分正负
        """
        if not nums: return 0
        size = len(nums)
        dp = [0 for _ in range(size)]
        dp[0] = nums[0]
        for i in range(1, size):
            if dp[i-1] >= 0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)

    def maxSubArray_2(self, nums: list) -> int:
        """不区分正负
        """
        if not nums: return 0
        size = len(nums)
        dp = [0 for _ in range(size)]
        dp[0] = nums[0]
        for i in range(1, size):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)
    
    def maxSubArray_3(self, nums: list) -> int:
        """空间优化
        """
        if not nums: return 0
        size = len(nums)
        cur_sum = nums[0]
        res = cur_sum
        for i in range(1, size):
            cur_sum = max(cur_sum+nums[i], nums[i])
            res = max(res, cur_sum)
        return res




if __name__ == "__main__":
    s = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(s.maxSubArray_2(nums))