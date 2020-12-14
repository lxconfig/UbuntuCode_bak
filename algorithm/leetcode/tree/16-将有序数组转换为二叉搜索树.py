

"""
    将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
    本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: list) -> TreeNode:
        """递归法
        实际上，题目的意思就是 已知树的中序遍历，还原树的结构
        由于数组是按升序排列的，所以数组中间的元素(实际上是中间元素的左边元素)肯定是根节点，其左边就是左子树，右边就是右子树
        而左右子树的的判断跟上面是一样的
        """
        def helper(left, right):
            if left > right: return None
            mid = (left + right) // 2    # 会向上取整，所以是左边元素
            root = TreeNode(nums[mid])
            root.left = helper(left,  mid - 1)
            root.right = helper(mid + 1, right)
            return root
        return helper(0, len(nums) - 1)
            