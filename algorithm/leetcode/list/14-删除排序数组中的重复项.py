

"""
    给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
    不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成
    你不需要考虑数组中超出新长度后面的元素。
"""


class Solution:
    def removeDuplicates(self, nums: list) -> int:
        """双指针法
            1. 定义count表示数组中不重复的数字的个数，同时，count表示慢指针
            2. 定义快指针i，从1开始到数组末尾
            3. 开始循环：
                3.1 当nums[count] == nums[i]时，i向后移动，跳过重复值
                3.2 当其不相等时，说明重复值已经全部跳过，此时i指向的值是下一个不重复的值，则count自增
                    并且，要将nums[i]的值赋给nums[count](即将这个不重复的值往前提，因为不需要考虑超出新长度的元素)
        """
        if not nums:
            return 0
        count = 0
        for i in range(1, len(nums)):
            if nums[count] != nums[i]:
                count += 1
                nums[count] = nums[i]
        return count + 1
    
    def removeDuplicates_2(self, nums):
        """倒着删除重复元素
        """
        if not nums: return 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i] == nums[i-1]:
                nums.pop(i)
        return len(nums)


if __name__ == "__main__":
    s = Solution()
    nums = [1,1,2]
    print(s.removeDuplicates_2(nums))