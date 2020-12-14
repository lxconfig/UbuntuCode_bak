

"""
    给定一个二叉树，返回它的前序、中序、后序、层次遍历
    递归算法很简单，你可以通过迭代算法完成吗？
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


""" 颜色标记法 """
def PreOrderTraversal(root):
    if not root: return []
    white, gray, ret = 0, 1, []
    stack = [(white, root)]
    while stack:
        color, node = stack.pop()
        if not node: continue
        if color == white:
            stack.append((white, node.right))
            stack.append((white, node.left))
            stack.append((gray, node))            
        else:
            ret.append(node.value)
    return ret


def InOrderTraversal(root):
    """
    将white为TreeNode数据类型，gray为int数据类型
        stack,rst = [root],[]
        while stack:
            i = stack.pop()
            if isinstance(i,TreeNode):
                stack.extend([i.right,i.val,i.left])
            elif isinstance(i,int):
                rst.append(i)
        return rst
    """
    if not root: return []
    white, gray, ret = 0, 1, []
    stack = [(white, root)]
    while stack:
        color, node = stack.pop()
        if not node: continue
        if color == white:
            # 白色表示没有访问过的节点
            stack.append((white, node.right))
            stack.append((gray, node))
            stack.append((white, node.left))
        else:
            # 灰色表示访问过
            ret.append(node.value)
    return ret


def PostOrderTraversal(root):
    if not root: return []
    white, gray, ret = 0, 1, []
    stack = [(white, root)]
    while stack:
        color, node = stack.pop()
        if not node: continue
        if color == white:
            stack.append((gray, node))
            stack.append((white, node.right))
            stack.append((white, node.left))
        else:
            ret.append(node.value)
    return ret


def levelOrder(root):
    """层次遍历 BFS
    """
    if not root: return []
    white, gray, ret, base_level = 0, 1, [], 0
    stack = [(white, root, base_level)]
    while stack:
        color, node, level = stack.pop(0)
        if not node: continue
        if color == white:
            stack.append((gray, node, level))
            stack.append((white, node.left, level+1))
            stack.append((white, node.right, level+1))
        else:
            if len(ret) == level: ret.append([])    # 对每一层新增一个[],用来保存该层的数
            ret[level].append(node.value)
    return ret


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list:
        """翻转法
        先按层次遍历做，最后奇偶翻转，得到结果
        """
        if not root: return []
        white, gray, ret, base_level = 0, 1, [], 0
        queue = [(white, root, base_level)]
        while queue:
            color, node, level = queue.pop(0)
            if not node: continue
            if color == white:
                queue.append((gray, node, level))
                queue.append((white, node.left, level + 1))
                queue.append((white, node.right, level + 1))                    
            else:
                if len(ret) == level: ret.append([])
                ret[level].append(node.val)
        
        for i in range(len(ret)):
            if i % 2 == 1:
                ret[i] = ret[i][::-1]
        return ret
    
    def zigzagLevelOrder_1(self, root: TreeNode) -> list:
        """用两个栈分别保存奇数层和偶数层的节点
        注：
            当某个节点访问完，要访问其左孩子或右孩子时，需要加到另一层中
            比如：1是偶数层节点，其孩子2，3就是奇数层节点
        """
        if not root: return []
        odd, even, ret = [], [root], []
        while odd or even:
            odd_node, even_node = [], []
            while even:
                node = even.pop()
                even_node.append(node.val)
                if node.left:
                    odd.append(node.left)
                if node.right:
                    odd.append(node.right)
            if even_node:
                ret.append(even_node)
            
            while odd:
                node = odd.pop()
                odd_node.append(node.val)
                if node.right:
                    even.append(node.right)
                if node.left:
                    even.append(node.left)
            if odd_node:
                ret.append(odd_node)
        return ret