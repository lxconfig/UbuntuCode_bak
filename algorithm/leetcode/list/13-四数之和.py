

"""
    给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？
    找出所有满足条件且不重复的四元组。答案中不可以包含重复的四元组。
"""


class Solution:
    def fourSum(self, nums: list, target: int) -> list:
        """
            1. 若nums的长度 n < 4或者nums为空，则可以直接返回[]
            2. 将nums数组排序
            3. 遍历排序后的数组
                3.1 对于nums中的重复元素，跳过，避免出现重复解
                3.2 再次遍历，目的在于找到四数中的第二个数，同样的，重复元素也要跳过
                3.3 记左指针left=j+1, 右指针right=n-1，当left < right时，循环：
                    3.3.1 若nums[i] + nums[j] + nums[left] + nums[right] == target, 将四数加入到res中，
                    判断left和right的下一位置是否重复(如：[-2,0,0,2,2])，并将left和right移到下一位置
                    3.3.2 若sums - target > 0, 说明right对应元素太大，right -= 1
                    3.3.3 若sums - target < 0, 说明left对应元素太小，left += 1
        """
        n = len(nums)
        if n < 4 or not nums:
            return []
        nums.sort()
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1, n):
                if j - i > 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    sums = nums[i] + nums[j] + nums[left] + nums[right]
                    if sums == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif sums - target > 0:
                        right -= 1
                    else:
                        left += 1
        return res

    def fourSum_2(self, nums: list, target: int) -> list:
        """
            上面的方法可以进一步优化：
            1. 第一次循环时，可以判断nums前四个数字之和 nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] 是否大于target
               若是的话，当前位置i，就不用继续计算了(因为是排序的，后面的数字只会更大，所以不可能之和是target)
            2. 第一次循环时，若i位置的值加上数组中最后三个数依旧小于target，那么当前位置的i也不用继续计算了(因为加上了最大的三个数，还是小于)

            同理：
                对第二次循环，可以进行上述两点优化

            注：
                优化后，循环的边界需要修改

        """
        n = len(nums)
        if n < 4 or not nums:
            return []
        nums.sort()
        res = []

        for i in range(n-3):
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                continue
            if i > 0 and nums[i] == nums[i - 1]:
                continue
        
            for j in range(i+1, n-2):
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                    continue
                if j - i > 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    sums = nums[i] + nums[j] + nums[left] + nums[right]
                    if sums == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif sums - target > 0:
                        right -= 1
                    else:
                        left += 1
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    print(s.fourSum_2(nums, 0))