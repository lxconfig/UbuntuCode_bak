

"""
    从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
    
    思路：
        层次遍历
"""



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # 
        if not pRoot:
            return []
        odd, even, ret = [], [pRoot], []
        while odd or even:
            tmps = []
            tmp = []
            while even:
                node = even.pop(0)
                tmps.append(node.val)
                if node.left:
                    odd.append(node.left)
                if node.right:
                    odd.append(node.right)
            if tmps:
                ret.append(tmps)
            
            while odd:
                node = odd.pop(0)
                tmp.append(node.val)
                if node.left:
                    even.append(node.left)
                if node.right:
                    even.append(node.right)
            if tmp:
                ret.append(tmp)
        return ret
    
    def Print2(self, pRoot):
        # 运行时间：23ms  占用内存：5624k
        if not pRoot:
            return []
        queue = [pRoot]
        ret = []
        while queue:
            tmp = []
            nextQueue = []
            for i in queue:
                tmp.append(i.val)
                if i.left:
                    nextQueue.append(i.left)
                if i.right:
                    nextQueue.append(i.right)
            queue = nextQueue
            ret.append(tmp)
        return ret


if __name__ == "__main__":
    a = TreeNode(8)
    b = TreeNode(7)
    c = TreeNode(4)
    d = TreeNode(3)
    e = TreeNode(9)
    f = TreeNode(6)
    g = TreeNode(5)
    h = TreeNode(11)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    f.left = h

    solution = Solution()
    print(solution.Print2(a))