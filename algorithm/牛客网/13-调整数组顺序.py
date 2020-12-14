
"""
    输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
    并保证奇数和奇数，偶数和偶数之间的相对位置不变。

"""


class Solution:
    def reOrderArray(self, array):
        # write code here
        '''
        # 以空间换时间
        # 运行时间：25ms  占用内存：5756k
        ret = []
        for i in array:
            if i & 1 == 1:
                # 奇数
                ret.append(i)
        for i in array:
            if i & 1 == 0:
                # 偶数
                ret.append(i)
        return ret
        '''
        # 运行时间：27ms  占用内存：5836k
        # 借助冒泡排序的思想
        for i in range(len(array)):
            for j in range(len(array)-i-1):
                if array[j] & 1 == 0 and array[j+1] & 1 == 1:
                    # 前偶后奇，则两个数要交换
                    array[j], array[j+1] = array[j+1], array[j]
        return array


if __name__ == "__main__":
    solution = Solution()
    print(solution.reOrderArray([1,2,3,4,5,6,7]))