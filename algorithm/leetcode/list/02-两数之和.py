

"""
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
"""


class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        """基于二分法的查找方法
        仅在nums数组有序的情况下才能成立
        """
        if not nums:
            return None
        low, high = 0, len(nums) - 1
        while low < high:
            if nums[low] + nums[high] == target:
                return [low, high]
            elif nums[low] + nums[high] < target:
                low += 1
            else:
                high -= 1
        return None

    def twoSum_2(self, nums: list, target: int) -> list:
        """字典法
        """
        if not nums:
            return None
        dicts = {}
        for i in range(len(nums)):
            j = target - nums[i]
            if j not in dicts:
                dicts[nums[i]] = i
            else:
                return [dicts[j], i]
    
    def twoSum_3(self, nums: list, target: int) -> list:
        if not nums: return []
        nums.sort()
        begin, end = 0, len(nums) - 1
        while begin < end:
            if nums[begin] + nums[end] == target:
                return [begin, end]
            elif nums[begin] + nums[end] > target:
                end -= 1
            else:
                begin += 1
        return []
        

if __name__ == "__main__":
    solution = Solution()
    nums = [3, 2, 4]
    target = 6
    print(solution.twoSum_3(nums, target))