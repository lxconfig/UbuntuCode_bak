

"""
    给定一个序列，求该序列中子序列乘积的最大值
    如： 2，3，-2，认为最大值是6
    max(i) = max(i-1) * a[i]  if a[i] >= 0
             min(i-1) * a[i]  if a[i] < 0
    
    min(i) = min(i-1) * a[i]  if a[i] >= 0
             max(i-1) * a[i]  if a[i] < 0
    
    max(i)表示当前第i个的最大值
    min(i)表示当前第i个的最小值
"""


def MaxProductSubarray(array):
    '''
    n = len(array)
    curmax, curmin, ret = 1, 1, -float("inf")
    for i in range(0, n):
        if array[i] < 0:
            curmax, curmin = curmin, curmax
        curmax = max(array[i] * curmax, array[i])
        curmin = min(array[i] * curmin, array[i])
        ret = max(curmax, ret)
    return ret
    '''
    """
    n = len(nums)
    max_list = [nums[0]] * n
    min_list = [nums[0]] * n
    for i in range(1, n):
        if nums[i] >= 0:
            max_list[i] = max_list[i-1] * nums[i]
            min_list[i] = min_list[i-1] * nums[i]
        else:
            max_list[i] = min_list[i-1] * nums[i]
            min_list[i] = max_list[i-1] * nums[i]
    return max(max_list)
    """
    n = len(array)
    res, curmax, curmin = array[0], array[0], array[0]
    for i in range(1, n):
        num = array[i]
        curmax, curmin = curmax * num, curmin * num
        curmax, curmin = max(curmax, curmin, num), min(curmax, curmin, num)
        res = curmax if curmax > res else res
    return res


if __name__ == "__main__":
    array = [2, 3, -2, 4]
    print(MaxProductSubarray(array))