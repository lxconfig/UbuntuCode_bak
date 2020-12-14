

# O(n^2)   不稳定
def selectionSort(array):
    """选择排序"""
    for i in range(len(array)):
        max_value_index = i   # 每次认为第i个是最大的元素的索引
        for j in range(i+1, len(array)):   # 每次开始比较的位置是i的下一个，因为不需要和自己比较
            if array[j] > array[max_value_index]:  # 若当前元素大，则修改索引
                max_value_index = j
        array[max_value_index], array[i] = array[i], array[max_value_index]
    return array


if __name__ == "__main__":
    array = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(selectionSort(array))