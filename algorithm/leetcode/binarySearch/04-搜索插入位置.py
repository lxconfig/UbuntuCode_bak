
"""
"""
from typing import List
import pysnooper


class Solution:
    # @pysnooper.snoop()
    def searchInsert(self, nums: List[int], target: int) -> int:
        """普通的二分查找
        """
        if not nums: return 0
        size = len(nums)
        left, right = 0, size - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def searchInsert_1(self, nums: List[int], target: int) -> int:
        """在循环体内部【排除】元素
        """
        if not nums: return 0
        size = len(nums)
        if target > nums[-1]: return size
        left, right = 0, size - 1
        while left < right:
            mid = (left + right) // 2
            # nums[mid]应该理解成：
            # nums[mid]是第一个大于target的数字，那么它的右边就肯定不是答案
            # nums[mid]刚好就是target
            # 所以搜索区间是 [left, mid]
            if nums[mid] >= target:
                right = mid
            # 而小于时，说明nums[mid]左边肯定不是答案
            # 所以搜索区间是 [mid + 1, right]
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    s = Solution()
    nums = [1, 3, 5, 6]
    target = 3
    print(s.searchInsert_1(nums, target))