
"""
    输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
    例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

    在列表的切片中，当索引值不存在时，不会报错，而是返回空值
    如: a = [1,2,3,4]
    a[5:] = []  a[1:5] = [2,3,4]

    运行时间：49ms
    占用内存：5736k
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # 递归函数的出口  结束条件
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        else:
            head = TreeNode(pre[0])
            index = tin.index(head.val)  # 找到根节点的索引值，方便划分
            # 左子树
            left_tin = tin[0:index]  
            left_pre = pre[1:len(left_tin)+1]

            # 右子树
            right_tin = tin[index+1:]  
            right_pre = pre[len(left_tin)+1:]

            head.left = self.reConstructBinaryTree(left_pre, left_tin)
            head.right = self.reConstructBinaryTree(right_pre, right_tin)

        return head


if __name__ == "__main__":
    solution = Solution()
    pre = [1,2,4,7,3,5,6,8]
    tin = [4,7,2,1,5,3,8,6]
    print(solution.reConstructBinaryTree(pre, tin))
