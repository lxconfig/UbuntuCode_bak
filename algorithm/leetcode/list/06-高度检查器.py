

"""
    学校在拍年度纪念照时，一般要求学生按照 非递减 的高度顺序排列。
    请你返回能让所有学生以 非递减 高度排列的最小必要移动人数。
"""
import copy

class Solution:
    def heightChecker(self, heights: list) -> int:
        """比较法
        将原数组和排序后的数组比较，若相同位置的元素值不等，则认为是要移动的人数
        """
        if not heights:
            return 0
        tmp = copy.deepcopy(heights)
        tmp.sort()
        count = 0
        for i in range(len(heights)):
            if heights[i] != tmp[i]:
                count += 1
        return count
    
    def heightChecker_2(self, heights: list) -> int:
        if not heights:
            return 0
        tmp = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != tmp[i]:
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    heights = [1,1,4,2,1,3]
    print(s.heightChecker_2(heights))