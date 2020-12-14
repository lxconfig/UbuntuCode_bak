

"""
    在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？
    例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子序列的和

    思路： DP
    f(i) = max(f(i-1)+a[i], a[i])    f(i)表示在选择某个数字时的最大值
    res = max(res, f(i))             res表示最终结果
"""


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        # 运行时间：22ms  占用内存：5852k
        # O(n)  time
        # O(1)  space
        arrayLen = len(array)
        if arrayLen < 2:
            return array[0]
        
        curmax = array[0]
        res = array[0]
        for i in range(1, arrayLen):
            curmax = max(curmax+array[i], array[i])
            res = max(res, curmax)
        
        return res


if __name__ == "__main__":
    solution = Solution()
    array = [1,-2,3,10,-4,7,2,-5]
    print(solution.FindGreatestSumOfSubArray(array))