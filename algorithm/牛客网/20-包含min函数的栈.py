
"""
    定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
    注意：保证测试中不会当栈为空的时候，对栈调用pop()或者min()或者top()方法。

    运行时间：29ms  占用内存：5688k

    思想：以空间换时间，从而保证min的时间复杂度是O(1)
"""


class Solution:
    def __init__(self):
        self.item = []
        self.minValue = []   # 每次保存的都是当前栈中最小的元素。如：当前栈=[1,2] 那么minValue=[1,1]

    def push(self, node):
        # write code here
        self.item.append(node)
        if self.minValue == []:
            self.minValue.append(node)
        else:
            if self.minValue[-1] > node:
                self.minValue.append(node)
            else:
                self.minValue.append(self.minValue[-1])   

    def pop(self):
        # write code here
        if self.item == []:
            return None
        self.minValue.pop()    # 要保证两个数组的长度一致。因为minValue数组保存的是栈再某个长度时的最小值
        return self.item.pop()
        
    def top(self):
        # write code here
        if self.item == []:
            return None
        return self.item[-1]

    def min(self):
        # write code here
        if self.minValue == []:
            return None
        return self.minValue[-1]


if __name__ == "__main__":
    pass