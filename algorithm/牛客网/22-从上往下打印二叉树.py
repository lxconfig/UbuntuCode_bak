


"""
    从上往下打印出二叉树的每个节点，同层节点从左至右打印。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # BFS  广度优先遍历
        # 运行时间：20ms  占用内存：5860k
        if not root:
            return []
        queue = [root]
        ret = []
        while queue:
            cur_node = queue.pop(0)
            ret.append(cur_node.val)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        return ret







if __name__ == "__main__":
    pass