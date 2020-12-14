
'''
    在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
    请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数

    运行时间：240ms
    占用内存：5860k
'''


class Solution:
    def Find(self, target, array):
        # 暴力搜索法
        # for i in array:
        #     if i:
        #         for j in i:
        #             if j == target:
        #                 return True
        # return False

        # 比较法
        i, j = 0, len(array[0]) - 1
        while i <= len(array)-1 and j >= 0:
            if target > array[i][j]:
                i = i + 1
            elif target < array[i][j]:
                j = j - 1
            else:
                return array[i][j]
        return False



if __name__ == "__main__":
    s = Solution()
    target = 2
    array = [[1,2,3], [4,5,6]]
    print(s.Find(target, array))