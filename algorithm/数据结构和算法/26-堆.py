
def heapify(array, length, parent):
    """调整数组，使之变成一个大根堆
    找到当前parent节点的两个child节点
    然后比较三者的大小，并交换
    """
    if parent >= length:
        # 递归出口
        return
    left_child = 2 * parent + 1
    right_child = 2 * parent + 2
    max_value = parent
    # 还需要判断两个child是否存在，即index值是否越界
    # 改成< 就是小根堆
    if left_child < length and array[left_child] > array[max_value]:
        max_value = left_child
    if right_child < length and array[right_child] > array[max_value]:
        max_value = right_child
    if max_value != parent:
        # 当最大者不是parent节点时才交换
        array[max_value], array[parent] = array[parent], array[max_value]
        # 然后递归，判断下一个子树
        heapify(array, length, max_value)

def build_heap(array, length):
    """建立一个堆
    从最后一个节点的parent节点开始构建堆,之后依次遍历到第一个节点
        parent = (i - 1) // 2
        left_child = 2 * parent + 1
        right_child = 2 * parent + 2
        O(n)  time
    """
    last_node = length - 1
    parent = (last_node - 1) // 2
    for i in range(parent, -1, -1):
        heapify(array, length, i)


def heapSort(array, length):
    """堆排序
    先交换堆顶元素和最后一个元素
    再删除并弹出最后一个元素(即原来的堆顶)
    再调整堆
    """
    build_heap(array, length)
    for i in range(length-1, -1, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)


if __name__ == "__main__":
    array = [4,5,1,6,2,7]
    length = len(array)
    # heapify(array, length, 0)

    heapSort(array, length)
    for i in range(length):
        print(array[i], end=" ")