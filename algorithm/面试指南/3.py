
while True:
    try:
        m, target = [int(x) for x in input().split(" ")]
        arr = [int(x) for x in input().split(" ")]
        left, right = 0, m - 1
        while left < right:
            sums = arr[left] + arr[right]
            if sums > target: right -= 1
            elif sums < target: left += 1
            else:
                print(arr[left], arr[right])
                while arr[left] == arr[left + 1]:
                    left += 1
                while arr[right] == arr[right - 1]:
                    right -= 1
                left, right = left + 1, right - 1
    except:
        break