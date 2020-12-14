

"""
    给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
    不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
    元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
"""


class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        """删除法
            从后遍历整个数组，判断是否和val相等，是则删除，否则跳过
        """
        if not nums:
            return 0
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
        return len(nums)
    
    def removeElement_2(self, nums: list, val: int) -> int:
        """
            1. 先将数组排序
            2. 然后找到数组中的第一个val和最后一个val
            3. 再删掉这个范围的val
        """
        if not nums: return 0
        nums.sort()
        first = self.FindFirstVal(nums, val)
        last = self.FindLastVal(nums, val)
        if first == -1 and last == -1:
            return len(nums)
        del nums[first: last + 1]
        return len(nums)

    def FindFirstVal(self, nums, val):
        length = len(nums)
        l, r = 0, length - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < val:
                l = mid + 1
            elif nums[mid] > val:
                r = mid - 1
            else:
                if (mid - 1) >= 0 and nums[mid - 1] == val:
                    r = mid - 1
                else:
                    return mid
        return -1

    def FindLastVal(self, nums, val):
        length = len(nums)
        l, r = 0, length - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < val:
                l = mid + 1
            elif nums[mid] > val:
                r = mid - 1
            else:
                if (mid + 1) <= r and nums[mid + 1] == val:
                    l = mid + 1
                else:
                    return mid
        return -1


    def removeElement_3(self, nums, val):
        """
            当遇到nums[i] == val时，将nums最后一个值赋值给nums[i]
            并将nums的长度n减一，达到删除val的目的，否则i加一
        """
        # if not nums: return 0
        # i = 0
        # for j in range(1, len(nums)):
        #     if val != nums[j]:
        #         nums[i] = nums[j]
        #         i += 1
        # return i + 1

        if not nums: return 0
        i, n = 0, len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n



if __name__ == "__main__":
    s = Solution()
    nums = [0,1,2,2,3,0,4,2]
    print(s.removeElement_3(nums, 2))