

"""
    在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
    输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
    题目保证输入的数组中没有的相同的数字
"""
# 运行时间：3106ms  占用内存：23052k
# import pysnooper


p = 0
class Solution:
    def InversePairs(self, data):
        global p
        # @pysnooper.snoop(output="./log.log", watch=("p"), overwrite=True)
        def mergeSort(data):
            global p
            length = len(data)
            if length == 1:
                return data
            gap = length >> 1
            left = mergeSort(data[:gap])
            right = mergeSort(data[gap:])

            ret = []
            l, r = 0, 0
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    ret.append(left[l])
                    l += 1
                else:
                    ret.append(right[r])
                    r += 1
                    p += len(left) - l     # 减去指针l 不是减去1. 因为左边可能并不是全都大于右边

            ret += right[r:]
            ret += left[l:]
            return ret
        mergeSort(data)
        return p % 1000000007


if __name__ == "__main__":
    solution = Solution()
    data = [1,2,3,4,5,6,7,0]
    print(solution.InversePairs(data))
