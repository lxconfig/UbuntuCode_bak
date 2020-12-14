

"""
    统计一个数字在排序数组中出现的次数。
"""


class Solution:
    def GetNumberOfK(self, data, k):
        # 运行时间：26ms  占用内存：5864k
        dataLen = len(data)
        if dataLen == 0:
            return 0
        ret = dict()
        ret[k] = 0
        for i in data:
            if i not in ret:
                ret[i] = 1
            else:
                ret[i] += 1
        return ret[k]
    
    def GetNumberOfK2(self, data, k):
        # 二分法, 找到数组中最后一个k的位置和第一个k的位置，相减加一即是k的个数
        # 运行时间：25ms  占用内存：5856k
        if not data:
            return 0
        first = self.FindFirstK(data, k)
        last = self.FindLastK(data, k)
        if  first == -1 and last == -1:
            return 0
        return last - first + 1
        
    def FindFirstK(self, data, k):
        """找到第一个k的位置"""
        dataLen = len(data)
        low, high = 0, dataLen - 1
        while low <= high:
            mid = (low + high) // 2
            if data[mid] < k:
                low = mid + 1
            elif data[mid] > k:
                high = mid - 1
            else:
                if (mid - 1) >= 0 and data[mid - 1] == k:
                    # 说明当前找到的mid位置不是第一个k的位置(因为前一个位置的元素就是k)
                    high = mid - 1
                else:
                    # 否则说明当前mid位置就是第一个k的位置
                    return mid
        return -1  # 表示没找到
    
    def FindLastK(self, data, k):
        """找到最后一个k的位置"""
        dataLen = len(data)
        low, high = 0, dataLen - 1
        while low <= high:
            mid = (low + high) // 2
            if data[mid] < k:
                low = mid + 1
            elif data[mid] > k:
                high = mid - 1
            else:
                if (mid + 1) <= high and data[mid + 1] == k:
                    # 说明当前找到的mid位置不是最后一个k的位置(因为后一个位置的元素就是k)
                    low = mid + 1
                else:
                    # 否则说明当前mid位置就是最后一个k的位置
                    return mid
        return -1  # 表示没找到


if __name__ == "__main__":
    solution = Solution()
    data = [1,3,3,3,3,4,5]
    print(solution.GetNumberOfK2(data, 3))