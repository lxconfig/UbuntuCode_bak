

# O(n^2)  稳定的
def insertSort(array):
    """插入排序"""
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j-1], array[j] = array[j], array[j-1]
            else:
                # 当没有进行上面的交换时，说明此元素就是在这个位置，那也就不用再对前面排好的元素比较
                # 如 i=2时，93不用交换，那么就退出本次循环
                break
    return array


if __name__ == "__main__":
    array = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(insertSort(array))