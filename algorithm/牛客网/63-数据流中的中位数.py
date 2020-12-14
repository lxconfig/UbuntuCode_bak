

"""
    如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
    如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
    我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。

    思路：
        用一个小顶堆，一个大顶堆来保存数据流
"""


import heapq


class Solution:
    def __init__(self):
        self.item = []
        self.minHeap = []
        self.maxHeap = []
        self.count = 0   # 元素个数

    def Insert(self, num):
        # write code here
        self.item.append(num)

    def GetMedian(self):
        # write code here
        if not self.item:
            return None
        length = len(self.item)
        self.item.sort()
        if length & 1 == 1:
            # 奇数
            return float(self.item[length >> 1])
        else:
            # 偶数
            mid = length >> 1
            return float((self.item[mid] + self.item[mid-1]) / 2)
            # return (self.item[mid] + self.item[mid-1]) / 2.0  python2版本

    # def insert(self, num):
    #     if self.count & 1 == 0:
    #         # 偶数
    #         heapq.heappush(self.maxHeap, num)
    #         max_value = heapq.heappop(self.maxHeap)
    #         heapq.heappush(self.minHeap, max_value)
    #     else:
    #         heapq.heappush(self.minHeap, num)
    #         min_value = heapq.heappop(self.maxHeap)
    #         heapq.heappush(self.maxHeap, min_value)

    # def getmedian(self):
    #     pass



if __name__ == "__main__":
    solution = Solution()
    solution.Insert(5)
    solution.Insert(2)
    # solution.Insert(3)

    print(solution.GetMedian())
