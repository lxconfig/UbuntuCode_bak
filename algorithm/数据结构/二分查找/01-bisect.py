
import bisect


arr = [1, 3, 4, 5, 6, 8, 9]
print(bisect.bisect(arr, 3))
print(bisect.bisect_left(arr, 3))
print(bisect.bisect_right(arr, 7))



def find(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target: left = mid + 1
        else: right = mid
    # 需要判断一下left是不是大于等于target的，否则如果target大于所有数字，返回left就不对
    return left if arr[left] >= target else left + 1


print(find(arr, 3))