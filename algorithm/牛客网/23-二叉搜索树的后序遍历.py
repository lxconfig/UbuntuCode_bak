

"""
    输入一个非空整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

    思路：后续遍历中的结果S中，最后一个元素一定是这棵树的根节点root，假设除去根节点root的序列为T
    又因为树是二叉搜索树，所以再T中，一定可以找到这样两个部分: 
        第一部分是左子树的节点，特点是都比root小
        第二部分是右子树的节点，特点是都比root大
    然后递归上面的过程即可判断
"""
import copy

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # 递归方法
        # 运行时间：20ms  占用内存：5732k
        if not sequence:
            return False
        
        root = sequence[-1]   # 根节点
        length = len(sequence)
        index = 0   # 两部分的分界点
        # 判断左子树
        for i in range(length-1):
            if sequence[i] <= root:
                index += 1
            else:
                break   # 表示左子树已经结束
        # 判断右子树
        for j in range(index, length-1):
            if sequence[j] < root:   # 在右子树中，如果数组的值小于root，说明非法
                return False
        left = True
        if index > 0:    # 当index <= 0 说明没有左子树，不需要递归
            left = self.VerifySquenceOfBST(sequence[:index])
        right = True
        if index < length - 1:   # 当index >= length-1 说明没有右子树，不需要递归
            right = self.VerifySquenceOfBST(sequence[index:(length-1)])
        
        return left and right

    def VerifySquenceOfBST2(self, sequence):
        """根据栈的压入和弹出序列来判断
        二叉搜索树的中序遍历是一个有序的数组
        如果把中序遍历看作是入栈序列，那么后序遍历是其一个可能的出栈序列
        """
        # 运行时间：30ms  占用内存：5840k
        push_sequence = copy.deepcopy(sequence)
        push_sequence.sort()
        stack = []
        index = 0
        for i in range(len(sequence)):
            stack.append(push_sequence[i])
            while stack and stack[-1] == sequence[index]:
                stack.pop()
                index += 1
        return stack == []

         



if __name__ == "__main__":
    pass