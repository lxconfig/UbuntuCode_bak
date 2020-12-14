


"""
"""

from typing import List


class Solution:
    def intervalSchedule(self, intvs: List[List[int]]) -> int:
        tmp = sorted(intvs, key=lambda x: x[1])
        count, x = 1, tmp[0]
        for item in tmp[1: ]:
            if item[0] >= x[1]:
                count += 1
                x = item
        return count
        




if __name__ == "__main__":
    s = Solution()
    intvs = [[1,2], [2,3], [3,4], [1,3]]
    print(s.intervalSchedule(intvs))