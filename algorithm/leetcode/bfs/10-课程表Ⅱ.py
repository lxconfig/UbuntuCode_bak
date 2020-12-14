

"""
"""

from typing import List
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites: return [i for i in range(numCourses)]
        # 创建入度数组和邻接表
        in_degrees = [0 for _ in range(numCourses)]
        adj = [set() for _ in range(numCourses)]
        # 初始化入度数组和邻接表
        for post, prev in prerequisites:
            in_degrees[post] += 1
            adj[prev].add(post)
        # 创建队列，把入度为0的节点加入队列
        queue, res = deque(), []
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)
        # 开始循环
        while queue:
            node = queue.popleft()
            res.append(node)
            for neighbor in adj[node]:
                # 所有邻接节点入度减1，若入度为0，则加入队列
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)
        if len(res) != numCourses: return []    
        return res


if __name__ == "__main__":
    s = Solution()
    numCourses, prerequisites = 4, [[1,0],[2,0],[3,1],[3,2]]
    print(s.findOrder(numCourses, prerequisites))   