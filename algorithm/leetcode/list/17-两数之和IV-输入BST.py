

"""
    给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        """
            先按中序遍历得到BST的遍历序列，再根据该序列进行二分搜索，确定是否存在和为target的两个元素
        """
        if not root: return False
        order = self.Inorder(root)
        n = len(order)
        left, right = 0, n - 1
        while left < right:
            temp = order[left] + order[right]
            if temp == k:
                return True
            elif temp < k:
                left += 1
            else:
                right -= 1
        return False

    def Inorder(self, root):
        if not root: return None
        stack, ret, node = [], [], root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                ret.append(node.val)
                node = node.right
        return ret

    def findTarget_2(self, root: TreeNode, k: int) -> bool:
        """遍历整棵树，找出所有可能的组合
        若x + y = k, 假设x是数中的一个节点值，只要再树中找到值为y = k - x的节点即可
        对于每个值为p的节点，再set中检查是否存在k-p，若存在，则找到，否则，将p加入到set中
        """
        def find(root, k, sets):
            if not root: return False
            if k - root.val in sets:
                return True
            sets.add(root.val)
            return find(root.left, k, sets) or find(root.right, k, sets)

        if not root: return False
        sets = set()
        return find(root, k, sets)

    def findTarget_3(self, root: TreeNode, k: int) -> bool:
        """广度优先搜索
        1. 从队列首部删除一个元素 p。
        2. 检查 set 中是否存在 k-p。如果存在，返回 True。
        3. 否则，将 p 加入 set。然后将当前节点的左孩子和右孩子加入 queue。
        4. 重复步骤一至三，直到 queue为空。
        5. 如果 queue 为空，返回 False。
        set用于保存已经访问过的节点
        """
        if not root: return False
        sets, queue = set(), [root]
        while queue:
            node = queue.pop(0)
            if k - node.val in sets:
                return True
            sets.add(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False


if __name__ == "__main__":
    s = Solution()
    a = TreeNode(5)
    b = TreeNode(3)
    c = TreeNode(6)
    d = TreeNode(2)
    e = TreeNode(4)
    f = TreeNode(7)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    print(s.findTarget_3(a, 9))