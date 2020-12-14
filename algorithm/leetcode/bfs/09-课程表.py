"""
"""

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """拓扑排序
        """
        # 入度数组
        in_degrees = [0 for _ in range(numCourses)]
        # 邻接表，set()是为了去重使用
        adj = [set() for _ in range(numCourses)]
        # 步骤一：初始化邻接表和入度数组
        # (0, 1)表示1 -> 0，先学1才能学2
        for post, prev in prerequisites:
            in_degrees[post] += 1
            adj[prev].add(post)
        # 步骤二：先把所有入度为0的节点加入队列
        queue, count = [], 0
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)
        while queue:
            node = queue.pop(0)
            count += 1
            # 步骤三：把node节点所有邻接节点的入度-1，若-1后入度为0，则加入队列
            for neighbor in adj[node]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)
        return count == numCourses


if __name__ == "__main__":
    s = Solution()
    numCourses, prerequisites = 3, [[1,0]]
    print(s.canFinish(numCourses, prerequisites))            