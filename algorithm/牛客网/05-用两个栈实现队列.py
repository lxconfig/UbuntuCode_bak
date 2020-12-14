

"""
    用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型

    用一个数组来模拟入队，一个数组来模拟出队
"""


class Stack:
    """定义栈"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        if self.items == []:
            return True
    
    def push(self, node):
        # insert可以对重复位置插入，旧的值会往后挪  a = [1]  a.insert(0, 2)  a = [2, 1]
        self.items.insert(0, node)
        return True
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return False

# 初始化两个空栈
stack_a = Stack()
stack_b = Stack()


class Solution:
    # 运行时间：27ms  占用内存：5708k
    # def __init__(self):
    #     self.items = []

    # def push(self, node):
    #     # 先入栈a，再出栈，再入栈b，再出栈b，就是队列先进先出的效果
    #     stack_a.push(node)
    #     stack_b.push(stack_a.pop())
    #     self.items.append(stack_b.pop())

    # def pop(self):
    #     # return xx
    #     return self.items.pop(0)

    # 运行时间：22ms  占用内存：5840k
    def __init__(self):
        self.a = []
        self.b = [3,4]
    
    def push(self, node):
        self.a.append(node)
    
    def pop(self):
        # 第二个栈必须都清空的情况下，才能把第一个栈的元素导进来
        if self.b == []:
            while self.a:
                self.b.append(self.a.pop(0))
            return self.b.pop(0)
        return self.b.pop(0)


if __name__ == "__main__":
    solution = Solution()
    solution.push(0)
    solution.push(1)
    solution.push(2)

    print(solution.pop())
    print(solution.pop())
    print(solution.pop())