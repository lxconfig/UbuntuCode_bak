

"""
    在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 
    例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

    思路：
        由于数组中的数字一定是在 0 - n-1 范围内
        所以可以去开辟一个新的数组tmp，元素全为False
        然后遍历numbers数组，将其中的元素，作为新数组tmp的索引位置，并置为True，代表访问过
        下次再遇到True时，说明是重复值
    或者：
        哈希表法(字典)
"""


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # 运行时间：22ms  占用内存：5628k
        if not numbers:
            return False
        tmp = [False] * len(numbers)
        for i in numbers:
            if tmp[i] == False:
                tmp[i] = True
            else:
                duplication[0] = i
                return True
        return False
    
    def duplicate2(self, numbers, duplication):
        # 运行时间：运行时间：26ms  占用内存：5724k
        if not numbers:
            return False
        dicts = {}
        for i in numbers:
            if i not in dicts:
                dicts[i] = 0
            else:
                dicts[i] += 1
        for i in numbers:
            if dicts[i] != 0:
                duplication[0] = i
                print(duplication)
                return True
        return False


if __name__ == "__main__":
    solution = Solution()
    array = [2,1,3,1,4]
    print(solution.duplicate2(array, [1]))