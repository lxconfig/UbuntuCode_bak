



def findFirstGreatAndEqualTargetIndex(arr, target):
    """
    找到数组中第一个大于等于target的索引
    """
    n = len(arr)
    if arr[n - 1] < target:
        return -1
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    print(left)
    return left

def findFirstGreatThanTarget(arr, target):
    """
    找到数组中第一个严格大于target的索引
    """
    n = len(arr)
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target: left = mid + 1
        else: right = mid
    print(left)
    return left


def findFirstLowAndEqualTargetIndex(arr, target):
    """
    找到数组中第一个小于等于target的索引
    """
    n = len(arr)
    left, right = 0, n - 1
    while left < right:
        mid = (left + right + 1) // 2
        if arr[mid] > target: right = mid - 1
        else: left = mid
    print(left)
    return left   

def findFirstLowThanTarget(arr, target):
    """
    找到数组中第一个严格小于target的索引
    """
    n = len(arr)
    left, right = 0, n - 1
    while left < right:
        mid = (left + right + 1) // 2
        if arr[mid] >= target: right = mid - 1
        else: left = mid
    print(left)
    return left

arr = [1, 2, 3, 5, 6]
target = 4

findFirstGreatAndEqualTargetIndex(arr, target)
findFirstGreatThanTarget(arr, target)
findFirstLowAndEqualTargetIndex(arr, target)
findFirstLowThanTarget(arr, target)