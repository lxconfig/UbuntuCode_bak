

"""
"""



# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        queue, res = deque(), []
        queue.append((0, root))
        while queue:
            level, node = queue.popleft()
            if len(res) == level: res.append([])
            res[level].append(node)
            if node.left:
                queue.append((level + 1, node.left))
            if node.right:
                queue.append((level + 1, node.right))
        
        for item in res:
            if len(item) == 1:
                item[0].next = None
            for i in range(1, len(item)):
                prev, post = item[i - 1], item[i]
                prev.next = post
        return res[0][0]

    def connect_1(self, root: 'Node') -> 'Node':
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i < size - 1:
                    node.next = queue[0]
        return root