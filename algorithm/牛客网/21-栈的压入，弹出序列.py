

"""
    输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。
    例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
    （注意：这两个序列的长度是相等的）

    运行时间：22ms  占用内存：5740k

    1. 首先要有一个栈
    2. 按照pushV的方式入栈
    3. 按照popV的方式出栈，出栈时需要循环判断是否需要出栈
    4. 判断是否需要出栈的时机：刚刚入栈就要判断
    5. 判断是否需要出栈的条件：入栈的那个元素是否等于出栈序列的顶部元素
"""


class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if pushV == [] or len(pushV) != len(popV):
            return None
        stack = []
        index = 0
        for i in range(len(pushV)):
            stack.append(pushV[i])  # 先入栈
            # 有可能栈当前只有一个元素，然后刚好也是出栈序列第一个元素，就会从stack中pop掉，所以要判断stack是否为空
            # 如果当前栈顶元素==出栈序列第一个元素，则栈顶元素出栈，同时还要判断栈内其他元素是否==出栈序列下一个元素
            # 如：入栈序列12345  出栈序列43521
            # 当前stack=[1 2 3 4], 4要出栈，由于3也可能出栈，所以要接着判断，所以用while循环
            while stack and stack[-1] == popV[index]:
                stack.pop()       # 如果入栈的那个值和出栈序列中的值相等，说明要出栈
                index += 1
        
        return stack == []


if __name__ == "__main__":
    pass

