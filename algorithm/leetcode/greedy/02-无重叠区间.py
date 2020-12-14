


"""
    给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def OverlapIntervals(intervals: List[List[int]]) -> int:
            if not intervals: return 0
            items = sorted(intervals, key=lambda x: x[1])
            x, count = items[0], 1
            for item in items[1: ]:
                if item[0] >= x[1]:
                    count, x = count + 1, item
            return count
        return len(intervals) - OverlapIntervals(intervals)