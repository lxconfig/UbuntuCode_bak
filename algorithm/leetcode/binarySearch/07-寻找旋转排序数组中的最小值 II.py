
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
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1
        return nums[left]


if __name__ == "__main__":
    s = Solution()
    nums = [2,2,2,0,1]
    print(s.findMin(nums))