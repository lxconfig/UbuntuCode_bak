

"""
    给定一个number，求树中的路径，使得路径上节点值之和等于number
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findPath(root, number):
    if not root:
        return []
    
    ret = []
    curNumber = 0
    path = []
    def helper(node, path, curNumber):
        curNumber += node.value
        path.append(node)
        isLeaf = node.left == None and node.right == None
        if curNumber == number and isLeaf:
            onePath = []
            for node in path:
                onePath.append(node.value)
            ret.append(onePath)
        if curNumber < number:
            if node.left:
                helper(node.left, path, curNumber)
            if node.right:
                helper(node.right, path, curNumber)
        # 如果当前curNumber > number
        # 说明刚刚插入path的节点不合适
        path.pop()
    helper(root, path, curNumber)
    return ret


if __name__ == "__main__":
    a = TreeNode(5)
    b = TreeNode(4)
    c = TreeNode(8)
    d = TreeNode(11)
    e = TreeNode(1)
    f = TreeNode(1)
    g = TreeNode(9)
    h = TreeNode(2)
    i = TreeNode(17)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    d.left = h
    f.left = i
    print(findPath(a, 22))