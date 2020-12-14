


"""
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                # 说明[mid, right]是递增的有序数列
                # 那么最小值不可能出现在这半部分，那么就可能在另一半
                # 而mid也有可能是最小值
                # 所以此时搜索区间应该是[left, mid]
                right = mid
            else:
                left = mid + 1
        return nums[left]


if __name__ == "__main__":
    s = Solution()
    nums = [3,4,5,6, 7,0,1,2]
    print(s.findMin(nums))