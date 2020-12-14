


def shellSort(array):
    """希尔排序"""
    n = len(array)
    gap = n // 2

    # 两个for循环就是插入排序，但是每次比较不是 前一个和后一个，而是相距gap的元素进行比较
    while gap:
        for i in range(gap, n):
            for j in range(i, 0, -1):
                if array[j] < array[j-gap]:
                    array[j], array[j-gap] = array[j-gap], array[j]
                else:
                    break     
        gap = gap // 2
    return array


if __name__ == "__main__":
    array = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(shellSort(array))