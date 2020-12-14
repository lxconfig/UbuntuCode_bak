
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def TreeInput():
    """接收树的输入
    可接收的形式是：
        3 1
        1 2 3
        2 0 0
        3 0 0
    第一行3和1分别代表： 树节点的个数，根节点的值
    后面每一行代表：节点值，左孩子，右孩子
    其中左孩子或右孩子为空，则输入的是0
    """
    n, root = [int(x) for x in input().split(" ")]
    tree = {root: TreeNode(root)}
    for _ in range(n):
        fa, lch, rch = [int(x) for x in input().split(" ")]
        if not tree.get(fa):
            tree[fa] = TreeNode(fa)
        if lch != 0 and not tree.get(lch):
            tree[lch] = TreeNode(lch)
            tree[fa].left = tree[lch]
        if rch != 0 and not tree.get(rch):
            tree[rch] = TreeNode(rch)
            tree[fa].right = tree[rch]


def OneRowInput():
    """接收一行输入
    4 5
    3 7
    输出：
    9
    10
    """
    while True:
        try:
            a, b = [int(x) for x in input().split(" ")]
            print(a + b)
        except:
            break

def ManyRowInput():
    """接收多行输入
    2       表示2行数据
    4 5
    3 7
    输出：
    9
    10
    """
    while True:
        try:
            t = int(input())
            for _ in range(t):
                a, b = [int(x) for x in input().split(" ")]
                print(a + b)
        except:
            break