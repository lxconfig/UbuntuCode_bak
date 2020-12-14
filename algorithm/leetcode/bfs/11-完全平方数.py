

"""
"""

class Solution:
    def numSquares(self, n: int) -> int:
        """dp
        """
        squares = [i ** 2 for i in range(1, int(n ** 0.5) + 1)]
        dp = [float("inf") for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            for square in squares:
                if square > i:
                    break                
                dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[n]

    def numSquares_1(self, n: int) -> int:
        """BFS
        """
        from collections import deque
        queue, depth = deque(), 1
        visited = set()
        queue.append(n)
        visited.add(n)
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                for j in range(1, int(node ** 0.5) + 1):
                    if j * j > node: continue
                    next_node = node - j * j
                    if next_node == 0:
                        return depth
                    if next_node not in visited:
                        queue.append(next_node)
                        visited.add(next_node)
            depth += 1
        return depth