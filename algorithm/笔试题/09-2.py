def helper(n, q, arr, num):
    min_diff = float("inf")
    for s in arr:
        diff = abs(num - s)
        min_diff = min(diff, min_diff)
    return min_diff
    # left, right = 0, n - 1
    # min_diff = float("inf")
    # while left < right:
    #     mid = (left + right) // 2
    #     diff = abs(num - arr[mid])
    #     if diff == 0: return arr[mid]
    #     if diff < min_diff:
    #         min_diff = diff
    #         right = mid - 1
    #     else:
    #         left = mid
    # return arr[left]
    

def findX():

    n, q = list(map(int, input().split(" ")))
    arr = list(map(int, input().split(" ")))
    # queries = []
    # for _ in range(n):
    #     queries.append(input())
    queries = [int(input()) for _ in range(n)]

    for num in queries:
        s = helper(n, q, arr, num)
        if s < 0: s = num - s
        elif s > 0: s = num - s
        else: s = num
        print(s, end=" ")


    

    
    

findX()
# n, q, arr, queries = findX()
# res = findDiff(n, q, arr, queries)
# print(res)