
"""
    输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。

    运行时间：25ms  占用内存：5752k
"""


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead == None:
            return None
        # 复制一个一样的node,并插入到之前链表中每一个元素的后面
        temp = pHead
        while temp:
            node = RandomListNode(temp.label)
            node.next = temp.next
            temp.next = node
            temp = node.next
        # 实现每个新建node的random指向
        temp = pHead
        # head = temp.next
        # while temp:
        #     if temp.random:
        #         temp.next.random = temp.random.next
        #     temp = temp.next.next
        cur = head = pHead.next
        while temp:
            if temp.random:
                cur.random = temp.random.next
                cur = temp.random.next
            temp = temp.next.next

        # 把复制出来node和原来的链表拆开
        temp = pHead
        cur = head
        while temp:
            temp.next = cur.next
            temp = temp.next
            if temp:
                cur.next = temp.next
                cur = cur.next
            # if cur.next:
            #     cur.next = cur.next.next
            #     cur = cur.next
            # temp = temp.next
        return head


if __name__ == "__main__":
    node1 = RandomListNode(1)
    node2 = RandomListNode(2)
    node3 = RandomListNode(3)
    node4 = RandomListNode(4)
    node5 = RandomListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    solution = Solution()
    head = solution.Clone(node1)
    temp = head
    while temp:
        print(temp.label)
        temp = temp.next