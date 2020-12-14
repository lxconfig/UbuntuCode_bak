
"""
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        size = len(nums)
        # 先找到旋转的点的索引
        index = 0
        for i in range(size - 1):
            if nums[i] > nums[i + 1]:
                index = i
        # 以旋转点为界，前半部分和后半部分都进行二分搜索
        prev = self.binarySearch(nums, 0, index, target)
        post = self.binarySearch(nums, index + 1, size - 1, target)
        if prev == post == -1: return -1
        return prev if prev != -1 else post
    
    def binarySearch(self, nums, left, right, target):
        if not nums: return -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def search_1(self, nums: List[int], target: int) -> int:
        if not nums: return -1 
        size = len(nums)
        left, right = 0, size - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # 当中间位置元素小于右边界元素时，说明[mid, right]是有序的
            # <=是因为while循环条件是left == right，而下面的写法，一定会出现left == right
            # 如果这里不写<=，那么就会死循环
            if nums[mid] <= nums[right]:
                # 如果满足条件，则说明target确实在(mid, right]区间内
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # 否则，target可能在[left, mid - 1]区间内
                else:
                    right = mid - 1
            # 同理，当中间位置元素大于左边界元素时，说明[left, mid]是有序的
            elif nums[left] <= nums[mid]:
                # 如果满足条件，说明target确实在[left, mid)区间内
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # 否则，target可能在[mid + 1, right]区间内
                else:
                    left = mid + 1
        return -1

    def search_2(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        size = len(nums)
        left, right = 0, size - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[right]:
                # 搜索区间是[mid, right]
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid - 1
            else:
                # 此时搜索区间是[left, mid - 1]
                if nums[left] <= target <= nums[mid - 1]:
                    right = mid - 1
                else:
                    left = mid
        return left if nums[left] == target else -1

    def search_3(self, nums: List[int], target: int) -> int:
        if not nums: return 0
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] == target: return mid
            if nums[mid] <= nums[right]:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid - 1
            else:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
        return left if nums[left] == target else -1


if __name__ == "__main__":
    s = Solution()
    nums = [3,1]
    target = 0
    print(s.search_2(nums, target))