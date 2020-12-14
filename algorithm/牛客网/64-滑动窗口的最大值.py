

"""
    给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，
    他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
    {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
"""


class Solution:
    def maxInWindows(self, num, size):
        # 运行时间：24ms 占用内存：5728k
        if not num:
            return []
        if size > len(num) or size <= 0:
            return []
        ret = []
        low, high = 0, size - 1
        while high < len(num):
            ret.append(max(num[low: high+1]))
            low += 1
            high += 1
        
        return ret


if __name__ == "__main__":
    solution = Solution()
    num = [10,14,12,11]
    size = 4
    print(solution.maxInWindows(num, size))
