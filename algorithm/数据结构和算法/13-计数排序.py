

"""
    计数排序适用于知道最大最小值的，以及数组中重复元素多的
"""


# def countSort(array):
#     """计数排序"""
#     # 先找到数组的最大、最小值
#     max_value, min_value = array[0], array[0]
#     for i in range(1, len(array)):
#         if array[i] > max_value:
#             max_value = array[i]
#         elif array[i] < min_value:
#             min_value = array[i]

#     # 新建一个数组，大小为len(array),范围是min_value-max_value
#     # 因为要能保存下最大值代表的索引
#     nums = [0] * (max_value - min_value + 1)
#     # print(nums)

#     # 把array里的数字，放到nums中对应的位置上
#     for i in range(len(array)):
#         # 还是为了能保存下最大值代表的索引，比如最大值9，最小值1，nums是一个大小为9的数组
#         # 无法保存最大值9代表的索引9,所以减去最小值
#         nums[array[i] - min_value] = nums[array[i] - min_value] + 1

#     pos = 0
#     for i in range(len(nums)):
#         for _ in range(nums[i]):
#             # 由于保存时减去了最小值，所以输出时要加回来
#             array[pos] = i + min_value
#             pos += 1
#     return array


# O(n)  不稳定
def countSort(array):
    # 先找到数组中的最值
    max_value, min_value = array[0], array[0]
    for i in range(1, len(array)):
        if array[i] < min_value:
            min_value = array[i]
        elif array[i] > max_value:
            max_value = array[i]
    
    # 生成一个大小为最值之差+1的数组
    length = max_value - min_value + 1
    nums = [0] * length

    # 将array数组中的数字，看作索引，在nums中+1
    for i in array:
        nums[i - min_value] = nums[i - min_value] + 1    # 就是把原数组的值，减去最小值，对应到新数组的索引上
    
    # 输出结果
    pos = 0
    for i in range(length):
        for _ in range(nums[i]):
            array[pos] = i + min_value      # 所以输出的时候要用索引+最小值
            pos += 1
    return array


if __name__ == "__main__":
    array = [2, 3,7,1,8,3,9,4]
    print(countSort(array))