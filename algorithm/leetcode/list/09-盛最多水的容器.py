
"""
    给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
    找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
"""


class Solution:
    def maxArea(self, height: list) -> int:
        """
            容量 = 高度 * 宽度
            容器装水的容量是由容器最短的高度决定的
            用两个指针分别指向数组的首元素和尾元素
            比较其元素大小，用较小的元素作为高度
            通过减小宽度，来计算出最大的盛水容量
        """
        if not height:
            return 0

        i, j, width, MaxArea = 0, len(height) - 1, len(height) - 1, 0

        for w in range(width, 0, -1):
            if height[i] > height[j]:
                # j减小，去找下一个可能较小的元素
                MaxArea, j = max(height[j] * w, MaxArea), j - 1
            else:
                # i增大，去找下一个可能较小的元素
                MaxArea, i = max(height[i] * w, MaxArea), i + 1
        
        return MaxArea


if __name__ == "__main__":
    s = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(s.maxArea(height))