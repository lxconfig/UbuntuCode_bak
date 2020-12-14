
"""
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
    输入: k = 3, n = 7
    输出: [[1,2,4]]
"""


from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n == 0: return [[]]
        begin, res, path = 1, [], []


        def dfs(begin, k, n, res, path):
            # 终止条件
            if n == 0:
                if len(path) == k:
                    res.append(path[:])
                    return 
            for i in range(begin, 10):
                # if n - i >= 0:
                path.append(i)
                dfs(i + 1, k, n - i, res, path)
                path.pop()
        
        dfs(begin, k, n, res, path)
        return res


if __name__ == "__main__":
    s = Solution()
    k, n = 3, 7
    print(s.combinationSum3(k, n))