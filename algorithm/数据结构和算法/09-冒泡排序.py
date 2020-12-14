import time
from functools import wraps


def Timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, *kwargs)
        end = time.time()
        print(end - start)
        return ret
    return wrapper


# O(n^2)
@Timer
def BubbleSort(array):
    """冒泡排序"""
    for i in range(len(array)):
        for j in range(len(array) - i -1):
            if array[j] > array[j+1]:    # 因为写的是j+1，所以内层循环要-1
                array[j], array[j+1] = array[j+1], array[j]
    return array


@Timer
def Better_BubbleSort(array):
    for i in range(len(array)):
        flag = False   # 优化，当array有序时，减少循环次数
        for j in range(len(array) - i -1):
            if array[j] > array[j+1]:    # 因为写的是j+1，所以内层循环要-1
                array[j], array[j+1] = array[j+1], array[j]
                flag = True
        if not flag:
            break
    return array


if __name__ == "__main__":
    array = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    array1 = [1,2,3,4,5]
    print(BubbleSort(array1))
    print(Better_BubbleSort(array1))