


"""
"""

from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # dp[K][i]表示经过K次中转，从起点src到终点i的航班价格
        dp = [[float("inf") for _ in range(K + 1)] for _ in range(n)]

        # 找到起点src直接能到达的地方，记录航班价格
        for flight in flights:
            if flight[0] == src:
                dp[flight[1]][0] = flight[2]

        # base case
        # 显然，从src到src是没有价格的，所以不管中转次数是多少，dp[i][K]都为0
        for i in range(K + 1):
            dp[src][i] = 0


        for k in range(1, K + 1):
            for flight in flights:
                if dp[flight[0]][k - 1] != float("inf"):
                    dp[flight[1]][k] = min(dp[flight[1]][k], dp[flight[0]][k - 1] + flight[2])

        return dp[dst][K] if dp[dst][K] != float("inf") else -1


if __name__ == "__main__":
    s = Solution()
    n, edges = 3, [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 1
    print(s.findCheapestPrice(n, edges, src, dst, k))