

"""
    给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
    注意：答案中不可以包含重复的三元组。
"""


class Solution:
    def threeSum(self, nums: list):
        """
        1. 首先，若nums的长度 n < 3，可以直接返回[]，因为没有三个数字
        2. 对数组排序
        3. 遍历排序后的数组：
            3.1 若nums[i] > 0: 直接返回，由于排好序了，那么nums[i]之后的值只会更大，肯定没有三数之和=0的情况
            3.2 对于nums中的重复元素，跳过，避免出现重复解
            3.3 记左指针left=i+1, 右指针right=n-1，当left < right时，循环：
                3.3.1 若 nums[i] + nums[left] + nums[right] = 0，判断left和right的下一位置是否重复(如：[-2,0,0,2,2])，并将left和right移到下一位置
                3.3.2 若和大于0，说明right太大，将right向左移
                3.3.3 若和小于0，说明left太小，将left向右移
        """
        n = len(nums)

        if n < 3:
            return []
        nums.sort()
        result = []
        for i in range(n):
            if nums[i] > 0:
                return result
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, n-1
            while left < right:
                sums = nums[i] + nums[left] + nums[right]
                if sums == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while(left < right and nums[left] == nums[left+1]):
                        left = left + 1
                    while(left < right and nums[right] == nums[right-1]):
                        right = right - 1
                    left = left + 1
                    right = right - 1
                elif sums > 0:
                    right -= 1
                else:
                    left += 1
        return result

    def threeSum_2(self, nums: list):
        if not nums: return []
        nums.sort()
        ret, n, i = [], len(nums), 0
        while i < n:
        # for循环是不能改变循环变量i的值，range()是一个迭代器，它只会输出信息，而不能修改迭代器的内容
        # 因此要改用while循环
        # for i in range(0, n):
            res = self.twoSum(nums, i + 1, 0-nums[i])
            for j in res:
                j.append(nums[i])
                j.sort()
                ret.append(j)
            # 跳过第一个数字重复的情况，否则出现重复结果
            while i < n - 1 and nums[i] == nums[i+1]: i += 1
            i += 1
        return ret

    def twoSum(self, nums, begin, target):
        end, res = len(nums) - 1, []
        while begin < end:
            # 记录每次索引begin和end最初的值，方便后面去重
            left, right = nums[begin], nums[end]
            if nums[begin] + nums[end] > target:
                while begin < end and nums[end] == right:
                    end -= 1
            elif nums[begin] + nums[end] < target:
                while begin < end and nums[begin] == left:
                    begin += 1
            else:
                res.append([left, right])
                while begin < end and nums[begin] == left: begin += 1
                while begin < end and nums[end] == right: end -= 1
        return res
        



if __name__ == "__main__":
    s = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(s.threeSum_2(nums))