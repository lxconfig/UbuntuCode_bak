
"""
"""


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return []
        queue, visited = [], {}
        queue.append(node)
        # 先克隆第一个节点
        # 每个克隆节点的邻居节点先设置为空
        visited[node] = Node(node.val, [])
        while queue:
            cur_node = queue.pop(0)
            for neighbor in cur_node.neighbors:
                if neighbor not in visited:
                    # 克隆邻居节点
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                # 克隆当前节点的邻居节点
                visited[cur_node].neighbors.append(visited[neighbor])
        return visited[node]