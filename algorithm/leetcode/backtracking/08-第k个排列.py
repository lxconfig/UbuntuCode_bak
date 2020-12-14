

"""
"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n == 0: return []
        used, res, path = [False for _ in range(n + 1)], [], []
        # 1-n的阶乘
        factorial = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            factorial[i] = factorial[i - 1] * i
        
        def dfs(used, k, res, begin):
            if begin == n:
                tmp_str = "".join(path[:])
                res.append(tmp_str)
                return 
            fac = factorial[n - begin]
            for i in range(1, n + 1):
                if used[i]: 
                    continue
                # 如果 k 大于这一个分支将要产生的叶子结点数，直接跳过这个分支，这个操作叫「剪枝」；
                # 如果 k 小于等于这一个分支将要产生的叶子结点数，那说明所求的全排列一定在这一个分支将要产生的叶子结点里，需要递归求解。
                if fac < k:
                    k -= fac
                    continue
                used[i] = True
                path.append(str(i))
                dfs(used, k, res, begin + 1)
                return 
        dfs(used, k, res, 0)
        return res[0]



if __name__ == "__main__":
    s = Solution()
    n, k = 3, 3
    print(s.getPermutation(n, k))