

from typing import List

class Solution:
    def binarySearch(self, nums: List[int], target: int):
        """二分查找
        """
        left, right = 0, len(nums) - 1
        while left <= right:     # *** 难点1 ***
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1   # *** 难点2 ***
            elif nums[mid] > target:
                right = mid - 1  # *** 难点3 ***
        return -1

    def FindLeftBound(self, nums: List[int], target: int):
        """寻找左侧边界
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        # 这里需要判断是否越界
        # target太大 or 太小都可能导致越界
        if left >= len(nums) or nums[left] != target:
            return -1
        return left
    
    def FindRightBound(self, nums: List[int], target: int):
        """寻找右侧边界
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        # target太小 or target太大
        if right < 0 or nums[right] != target:
            return -1
        return right


if __name__ == "__main__":
    s = Solution()
    target, nums = 2, [1, 2, 2, 2, 3, 4, 5]
    print("普通二分查找:", s.binarySearch(nums, target))
    print("寻找左侧边界:", s.FindLeftBound(nums, target))
    print("寻找右侧边界:", s.FindRightBound(nums, target))
    