


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        """自顶向下的递归
        需要添加备忘录，否则复杂度太高
        """
        def dp(K, N):
            if K == 1: return N
            if N == 0: return 0
            res = float("inf")
            for i in range(1, N+1):
                res = min(
                    res,
                    max(
                        dp(K-1, i-1),   # 鸡蛋碎了
                        dp(K, N-i)      # 鸡蛋没碎
                    ) + 1               # 在第i层扔鸡蛋，所以+1
                )
            return res
        return dp(K, N)

    def superEggDrop_1(self, K: int, N: int) -> int:
        """N=2000时还是会超时
        """
        memo = dict()
        def dp(K, N):
            if K == 1: return N
            if N == 0: return 0
            if (K, N) in memo: return memo[(K, N)]
            res = float("inf")
            for i in range(1, N+1):
                res = min(
                    res,
                    max(
                        dp(K-1, i-1),   # 鸡蛋碎了
                        dp(K, N-i)      # 鸡蛋没碎
                    ) + 1               # 在第i层扔鸡蛋，所以+1
                )
            memo[(K, N)] = res
            return res
        return dp(K, N)

    
    def superEggDrop_2(self, K: int, N: int) -> int:
        memo = dict()
        def dp(K, N):
            if K == 1: return N
            if N == 0: return 0
            if (K, N) in memo: return memo[(K, N)]
            res = float("inf")
            low, high = 1, N
            while low <= high:
                mid = (low + high) // 2
                broken = dp(K - 1, mid - 1)  # 鸡蛋碎了
                not_broken = dp(K, N - mid)  # 鸡蛋没碎
                if broken > not_broken:
                    high = mid - 1
                    res = min(res, broken + 1)  # 在mid层扔鸡蛋，所以+1
                else:
                    low = mid + 1
                    res = min(res, not_broken + 1)  # 在mid层扔鸡蛋，所以+1
            memo[(K, N)] = res
            return res
        return dp(K, N)


if __name__ == "__main__":
    s = Solution()
    K, N = 4, 2000
    print(s.superEggDrop_1(K, N))