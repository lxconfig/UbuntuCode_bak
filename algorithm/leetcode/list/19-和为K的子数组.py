

"""
    给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
    例：
        输入: nums = [1,1,1], k = 2
        输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
"""
import pysnooper

class Solution:
    # @pysnooper.snoop()
    def subarraySum(self, nums: list, k: int) -> int:
        """前缀和，然后暴力循环
        数据太多超时
        """
        if not nums: return 0
        n = len(nums)
        preSum = [0] * (n + 1)
        for i in range(n):
            preSum[i + 1] = preSum[i] + nums[i]

        count = 0
        for i in range(n):
            for j in range(i, n):
                sums = preSum[j + 1] - preSum[i]
                if sums == k:
                    count += 1
        return count

    def subarraySum_2(self, nums: list, k: int) -> int:
        """优化版
        1. 上面的方法中第二个for循环可以不要，它就是在计算某个范围的和而已，可以改成减法来做
        2. 前缀和可以不用开辟数组，仅计算当前的和
        3. 可以用字典来保存前缀和-k的差值
        """
        if not nums: return 0
        n = len(nums)
        hashmap = {}
        preSum = 0
        count = 0
        for i in range(n):
            preSum += nums[i]
            if preSum == k:
                count += 1
            if preSum - k in hashmap:
                count += hashmap[preSum - k]
            if preSum in hashmap:
                hashmap[preSum] += 1
            else:
                hashmap[preSum] = 1
        print(hashmap)
        return count


if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3]
    print(s.subarraySum_2(nums, 3))