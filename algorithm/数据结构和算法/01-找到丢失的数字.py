
'''
def main():
    """
        有n-1个数字，范围是[1-n]，数据不递增不重复，找到丢失的那个数字
    """
    temp = 0
    ret = 0
    lost_num_list = [1,3,4]
    # 范围是[1-4]
    for i in range(1, 5):
        temp = temp ^ i
    print(temp)
    for j in lost_num_list:
       ret = ret ^ j
    print(temp ^ ret)

    # for j in lost_num_list:
    #     num = temp ^ j
    #     temp = num
    # print(num)
'''

def find_missing_1_number(sequence, n):
    """ returns the missing number of sequence, which is supposed to be
    a permutation of {1,..,n} with one number missing.
    """
    x = n
    for i in range(1, n):
        x ^= i
    for e in sequence:
        x ^= e
    return x

import pysnooper

# @pysnooper.snoop()
def find_missing_2_number(array):
    """
        找到一个数组中丢失的两个数字，数组不排序
        此方法仅适用数组中最大数==数组长度的情况
    """
    for i in range(len(array)):
        index = abs(array[i]) - 1    # 取绝对值是因为，此时的array[i]可能已经被改成了负数
        array[index] = -abs(array[index])
    return [i + 1 for i in range(len(array)) if array[i] > 0]


if __name__ == "__main__":
    # main()
    print(find_missing_1_number([1, 3, 4], 4))

    print(find_missing_2_number([4,2,1,5,6,8,2,4]))

