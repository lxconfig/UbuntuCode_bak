

"""
    给定一个包含非负数的数组和一个目标整数 k，编写一个函数来判断该数组是否含有连续的子数组，其大小至少为 2，总和为 k 的倍数，
    即总和为 n*k，其中 n 也是一个整数。
"""


class Solution:
    def checkSubarraySum(self, nums: list, k: int) -> bool:
        """前缀和法
            开辟一个数组来记录前缀和
            注意： 前缀和记录的只是从0开始，一直到长度n的和
            如： [1,2,3]  其前缀和数组为[0, 1, 3, 6], 即0， 0+1， 0+1+2(index)
            所以，要双循环计算某个范围的和
            特别注意当k=0的情况
        """
        if not nums: return False
        n = len(nums)
        preSum = [0] * (n + 1)
        for i in range(n):
            preSum[i + 1] = preSum[i] + nums[i]
        for i in range(n):
            for j in range(i+1, n):
                sums = preSum[j + 1] - preSum[i]
                if sums == 0 and k == 0:
                    return True
                elif k != 0 and sums % k == 0:
                    return True
        return False

    def checkSubarraySum_2(self, nums, k):
        """优化版
            1. 前缀和不用全部保存，只需要记录好前面的和+当前值即可
            2. 用字典保存 前缀和%k: 出现这个前缀和的索引
        """
        hashmap = {0: -1} # key:preSum % k, value:index
        preSum = 0
        for i in range(len(nums)):
            preSum = preSum + nums[i]
            key = preSum if k == 0 else preSum % k
            if key in hashmap:
                if i - hashmap[key] > 1:   # 保证至少两个数
                    return True
            else:
                hashmap[key] = i
        # print(hashmap)
        return False


if __name__ == "__main__":
    s = Solution()
    nums = [0, 1, 0]
    print(s.checkSubarraySum_2(nums, 0))