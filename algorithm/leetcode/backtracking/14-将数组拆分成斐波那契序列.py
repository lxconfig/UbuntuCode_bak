
"""
"""

from typing import List


class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        size = len(num)
        if size < 3: return []
        self.res, path, begin = [], [], 0
        def dfs(num, begin, path):
            # 终止条件
            if len(path) >= 3 and begin == size:
                self.res = path
                return
            if begin == size:
                return
            for i in range(begin, size):
                if num[begin] == "0" and i > begin:
                    return 
                if int(num[begin: i + 1]) > 2 ** 31 - 1 or int(num[begin: i + 1]) < 0:
                    continue
                if len(path) < 2:
                    dfs(num, i + 1, path + [int(num[begin: i + 1])])
                else:
                    if int(num[begin: i + 1]) == path[-1] + path[-2]:
                        dfs(num, i + 1, path + [int(num[begin: i + 1])])
        dfs(num, begin, path)
        return self.res
        

if __name__ == "__main__":
    s = Solution()
    num = "1123"
    print(s.splitIntoFibonacci(num))