

"""
    给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
    返回这三个数的和。假定每组输入只存在唯一答案。
"""


class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        """类似三数之和的解法
        用字典保存每次的三数之和以及和target的距离(绝对值)
        再将字典排序，得到结果
        """
        if not nums:
            return 0
        n = len(nums)
        if n < 3:
            return 0
        ret = {}
        nums.sort()
        for i in range(n):
            left, right = i + 1, n - 1
            while left < right:
                sums = nums[i] + nums[left] + nums[right]
                dist = abs(target - sums)
                ret[sums] = dist
                if sums == target:
                    return target
                if sums - target > 0:
                    right -= 1
                else:
                    left += 1
        ret = sorted(ret.items(), key=lambda ret:ret[1])
        return ret[0][0]
    
    def threeSumClosest_2(self, nums: list, target: int) -> int:
        """
            1. 若nums的长度 n < 3，则直接返回
            2. 将nums排序，并定义res为无穷大，表示最小距离的和
            3. 定义left，right分别表示三数中的第二个数和第三个数，其中left = i + 1, right = n - 1, 开始循环：
                3.1 若三数之和sums = target, 可以直接返回target, 表示距离target最近
                3.2 计算sums到target的距离的绝对值，并和res到target的距离的绝对值比较，若更小，则更新res
                3.3 若距离 < 0, 说明left指向的值太小，left + 1
                3.4 若距离 > 0, 说明right指向的值太大，right - 1
            4. 最后返回res
        """
        if not nums:
            return 0
        n = len(nums)
        if n < 3:
            return 0
        nums.sort()
        res = float("inf")
        for i in range(n):
            left, right = i + 1, n - 1
            while left < right:
                sums = nums[i] + nums[left] + nums[right]
                if sums == target:
                    return target
                if abs(sums - target) < abs(res - target):
                    res = sums
                if sums - target < 0:
                    left += 1
                else:
                    right -= 1
        return res


if __name__ == "__main__":
    s = Solution()
    # nums = [1,2,4,8,16,32,64,128]
    nums = [-1,2,1,-4]
    print(s.threeSumClosest(nums, 1))