

"""
    输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。

    思路：双指针（滑动窗口）
"""
import pysnooper


class Solution:
    # @pysnooper.snoop()
    def FindNumbersWithSum(self, array, tsum):
        # 暴力法
        # 运行时间：30ms  占用内存：5716k
        if not array or tsum == 0:
            return []
        ret = []
        low, high = 0, 1
        while low < high and high < len(array):
            if array[low] + array[high] == tsum:
                if ret:
                    for i in ret:
                        if i[0] * i[1] > array[low] * array[high]:
                            ret.pop(0)
                            ret.append([array[low], array[high]])
                else:
                    ret.append([array[low], array[high]])
                low += 1
                high = low + 1
            elif array[low] + array[high] < tsum:
                high += 1
            else:
                low += 1
                high = low + 1

        return ret[0] if ret else []
    
    def FindNumbersWithSum2(self, array, tsum):
        """一头一尾双指针"""
        # 运行时间：28ms  占用内存：5852k
        if not array or tsum == 0:
            return []
        ret = []
        
        low, high = 0, len(array) - 1
        while low < high:
            # 找到了就可以直接return
            # 因为最先找到的肯定是乘积最小的(相隔最远)
            if array[low] + array[high] == tsum:
                ret.extend([array[low], array[high]])
                return ret
            elif array[low] + array[high] < tsum:
                low += 1
            else:
                high -= 1
        return []


if __name__ == "__main__":
    array = [1,2,4,7,11,13, 15]
    solution = Solution()
    print(solution.FindNumbersWithSum2(array, 15))