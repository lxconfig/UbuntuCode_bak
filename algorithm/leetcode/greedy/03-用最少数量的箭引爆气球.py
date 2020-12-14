

"""
"""

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        tmp = sorted(points, key= lambda x: x[1])
        count, x = 1, tmp[0]
        for item in tmp[1: ]:
            if item[0] > x[1]:
                count, x = count + 1, item
        return count