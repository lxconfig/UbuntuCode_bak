


"""
"""



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """BFS
        """
        if not root: return 0
        # 度至少为1
        queue, depth = [], 1
        queue.append(root)
        while queue:
            size = len(queue)
            for _ in range(size):
                # 这里不能每次都pop最后一个元素, 考虑[1,2,3,4,null,null,5]
                # 都pop最后一个元素的话，出队顺序是：135
                cur_node = queue.pop(0)
                if not cur_node.left and not cur_node.right:
                    return depth
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            depth += 1
        return depth
    
    def minDepth_1(self, root: TreeNode) -> int:
        """DFS
        """
        if not root: return 0
        stack, depth, min_depth = [], 1, float("inf")
        stack.append(root)
        while stack:
            size = len(stack)
            for _ in range(size):
                cur_node = stack.pop(0)
                if not cur_node.left and not cur_node.right:
                    depth = min(depth, min_depth)
                if cur_node.right:
                    stack.append(cur_node.right)
                if cur_node.left:
                    stack.append(cur_node.left)
            depth += 1
        return min_depth
