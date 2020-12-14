
""" 
    数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
    例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
"""


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # 暴力法，遍历每个数字，并记录次数
        # 运行时间：22ms  占用内存：5712k
        if len(numbers) == 0:
            return 0
        if len(numbers) == 1:
            return numbers[0]
        nums = dict()
        for num in numbers:
            if num in nums:
                nums[num] += 1
            else:
                nums[num] = 1
            if nums[num] > len(numbers) // 2:
                return num
        return 0
    
    def MoreThanHalfNum_Solution2(self, numbers):
        # 抵消法
        # 记录每个值及其出现的次数，当后一个值与当前值不等时，认为这两个值抵消掉(次数改为0，不是真的删除掉)
        # 最后剩的元素就可能是最多的元素，再循环一次就能判断
        ret = numbers[0]
        count = 1
        for i in numbers[1:]:
            if i == ret:
                count += 1
            else:
                count -= 1
            if count == 0:
                ret = i
                count = 1
        retCount = 0
        for i in numbers:
            if i == ret:
                retCount += 1
        return ret if retCount > len(numbers) // 2.0 else 0
    
    def MoreThanHalfNum_Solution3(self, numbers):
        # 排序法
        # 当一个数组有序时，其出现次数最多的元素肯定在中间位置
        numbers.sort()
        n = len(numbers) // 2
        return numbers[n]
        



if __name__ == "__main__":
    numbers = [1,2,3,2,2,2,5,4,2]
    solution = Solution()
    print(solution.MoreThanHalfNum_Solution(numbers))
    print(solution.MoreThanHalfNum_Solution2(numbers))
    print(solution.MoreThanHalfNum_Solution3(numbers))