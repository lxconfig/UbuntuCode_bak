

"""
    如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
    如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
    我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
"""


class Solution:
    def __init__(self):
        self.data = []

    def Insert(self, num):
        self.data.append(num)

    def GetMedian(self):
        # write code here
        if not self.data:
            return None
        
        length = len(self.data)
        self.data.sort()
        if length & 1 == 0:
            return (self.data[length >> 1] + self.data[(length >> 1) - 1]) / 2.0
        else:
            return self.data[length >> 1]


if __name__ == "__main__":
    s = Solution()
    s.Insert(5)
    s.Insert(2)
    s.Insert(3)
    s.Insert(4)
    print(s.GetMedian())