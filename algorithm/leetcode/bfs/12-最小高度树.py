
"""
"""

from typing import List
from collections import deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        queue, res = deque(), []
        in_degrees = [0 for _ in range(n)]
        adj = [set() for _ in range(n)]
        for n1, n2 in edges:
            in_degrees[n1] += 1
            in_degrees[n2] += 1
            adj[n1].add(n2)
            adj[n2].add(n1)

        # 先让度为1的节点入队列，度为1的节点就是叶子节点，高度为0
        for i in range(n):
            if in_degrees[i] == 1:
                queue.append(i)

        while queue:
            res = []
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                res.append(node)
                for neighbor in adj[node]:
                    in_degrees[neighbor] -= 1
                    if in_degrees[neighbor] == 1:
                        queue.append(neighbor)
        return res


if __name__ == "__main__":
    s = Solution()
    n = 6
    edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
    print(s.findMinHeightTrees(n, edges))