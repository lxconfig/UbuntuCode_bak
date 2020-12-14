


def quickSort(array):
    """快速排序"""
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        left = [i for i in array[1:] if i < pivot]
        right = [j for j in array[1:] if j > pivot]
        return quickSort(left) + [pivot] + quickSort(right)



if __name__ == "__main__":
    array = [54, 26, 93, 17, 77, 31, 44, 50, 20]
    print(quickSort(array))