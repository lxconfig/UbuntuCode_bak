

# O(nlogn)
def mergeSort(array):
    """归并排序"""
    # 利用分治法的思想，每次将数组拆成一半来操作
    length = len(array)
    if length == 1:
        return array
    # 拆分的过程
    gap = length // 2
    left = mergeSort(array[:gap])
    right = mergeSort(array[gap:])

    # 合并的过程
    ret = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            ret.append(left[l])
            l += 1
        else:
            ret.append(right[r])
            r += 1
    
    # 两边数组长度不等的情况
    while l < len(left):
        ret.append(left[l])
        l += 1
    
    while r < len(right):
        ret.append(right[r])
        r += 1
    return ret


if __name__ == "__main__":
    array = [54, 26, 93, 17, 77, 31, 44, 55, 20, 8, 21, 29, 1,20, 34]
    # array = [1,2,3,4,5,6,7,0]
    print(mergeSort(array))