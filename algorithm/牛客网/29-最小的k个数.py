

"""
    输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
"""

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # 排序法
        # O(nlogn)
        # 运行时间：39ms  占用内存：5844k
        if len(tinput) < k:
            return []
        
        tinput.sort()
        return tinput[:k]

    def GetLeastNumbers_Solution2(self, tinput, k):
        # 大顶堆
        # 将前k个元素建立成大顶堆，然后对其他n-k个元素依次检查
        # 若比堆顶元素大，则跳过不管
        # 若比堆顶元素小，则将堆顶元素与该元素交换，并调整堆，再次变成大顶堆
        # 最后堆中的元素就是k个最小的元素，排序之后返回
        # 运行时间：32ms  占用内存：5848k
        if len(tinput) < k or k < 0:
            return []
        self.heapSort(tinput, len(tinput))
        return tinput[:k]

    def heapify(self, array, length, parent):
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
            self.heapify(array, length, max_value)
    
    def build_heap(self, array, length):
        """建立一个堆
        从最后一个节点的parent节点开始构建堆,之后依次遍历到第一个节点
            parent = (i - 1) // 2
            left_child = 2 * parent + 1
            right_child = 2 * parent + 2
        """
        last_node = length - 1
        parent = (last_node - 1) // 2
        for i in range(parent, -1, -1):
            self.heapify(array, length, i)

    def heapSort(self, array, length):
        """堆排序
        先交换堆顶元素和最后一个元素
        再删除并弹出最后一个元素(即原来的堆顶)
        再调整堆
        """
        self.build_heap(array, length)
        for i in range(length-1, -1, -1):
            array[i], array[0] = array[0], array[i]
            self.heapify(array, i, 0)

    def GetLeastNumbers_Solution3(self, tinput, k):

        # 创建堆，或者插入元素到堆
        def createMaxHeap(num):
            maxHeap.append(num)
            currentIndex = len(maxHeap) - 1
            while currentIndex != 0:
                parentIndex = (currentIndex - 1) // 2
                if maxHeap[parentIndex] < maxHeap[currentIndex]:
                    maxHeap[currentIndex], maxHeap[parentIndex] = maxHeap[parentIndex], maxHeap[currentIndex]
                else:
                    break
        
        # 调整最大堆
        def adjustMaxHeap(num):
            if num < maxHeap[0]:
                maxHeap[0] = num
            index = 0
            maxHeapLen = len(maxHeap)
            while index < maxHeapLen:
                left_index = index * 2 + 1
                right_index = index * 2 + 2
                largerIndex = 0
                if right_index < maxHeapLen:
                    if maxHeap[right_index] < maxHeap[left_index]:
                        largerIndex = right_index
                    else:
                        largerIndex = left_index
                elif left_index < maxHeapLen:
                    largerIndex = left_index
                else:
                    break
                if maxHeap[index] < maxHeap[largerIndex]:
                    maxHeap[index], maxHeap[largerIndex] = maxHeap[largerIndex], maxHeap[index]
                index = largerIndex
        
        maxHeap = []
        inputLen = len(tinput)
        if inputLen < k or k <= 0:
            return []
        for i in range(inputLen):
            if i < k:
                createMaxHeap(tinput[i])
            else:
                adjustMaxHeap(tinput[i])
        return maxHeap


if __name__ == "__main__":
    tinput = [4,5,1,6,2,7,3,8]
    solution = Solution()
    # print(solution.GetLeastNumbers_Solution(tinput, 10))
    print(solution.GetLeastNumbers_Solution2(tinput, 7))