

"""
    用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""


class Solution:
    def __init__(self):
        self.a = []
        self.b = []

    def push(self, node):
        self.a.append(node)
        self.b.append(self.a.pop(0))
    
    def pop(self):
        return self.b.pop(0)