
def solution(arr):
    """最长上升子序列
    """
    size = len(arr)
    dp = [1 for _ in range(size)]
    # 数据特别大时，不适合用双循环，会超时
    # for i in range(1, size):
    #     for j in range(i):
    #         if arr[j] < arr[i]:
    #             dp[i] = max(dp[i], dp[j] + 1)
    for i in range(1, size):
        if arr[i] - arr[i - 1] == 0:
            dp[i] = dp[i - 1]
        if arr[i] - arr[i - 1] == 1:
            dp[i] = dp[i - 1] + 1
    return max(dp)
            

if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            arr = [int(x) for x in input().split(" ")]
            arr.sort()
            res = solution(arr)
            print(res)
        except:
            break