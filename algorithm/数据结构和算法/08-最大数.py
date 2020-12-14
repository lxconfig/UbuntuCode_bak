
"""
    给定一个数组，一个数组有且只有一个最大数，判断这个最大数是否是其他数字的两倍或更大，返回这个最大数的index，否则返回-1
"""
import pysnooper


@pysnooper.snoop()
def largest_twice_number(array):
    # 只需要找到最大数和第二大数，再比较就行
    maximum, second, index = array[0], array[0], 0
    for i in range(1, len(array)):
        if maximum < array[i]:
            second = maximum
            maximum = array[i]
            index = i
        elif second < array[i]:
            second = array[i]
    print(maximum, second)
    return index if maximum > 2*second else -1


if __name__ == "__main__":
    print(largest_twice_number([1,2,444,8,3,99,0]))