

"""
    你准备做兼职赚钱，有多种兼职工作可选，每种兼职工作赚的钱有多有少，同时兼职工作有时间要求
    求最大收益

    思路：认为有两种状态：选和不选
    dp[i] = max(
        dp[i-1],   不选时，认为收益就是前一个任务的收益
        value + dp[prev[i-1]]   选时，认为收益是当前这个任务的收益+之前还可以做的任务的收益
    )
    prev表示当选择第i个任务后，前面还有什么任务是可以做的，这里选的是前面最近的那个
"""
import pysnooper


# @pysnooper.snoop()
# O(n)  time
# O(n)  space
def MaxProfit(array):
    n = len(array)
    prev = [0] * n  # 确定当前做某个兼职时，前面还有哪个兼职是可以做的 [0, 0, 0, 1, 0, 2, 3, 5]
    for i in range(1, n):
        for j in range(i, 0, -1):
            if array[i][0] >= array[j-1][1]:
                prev[i] = j
                break
    dp = [0] * (n+1)
    for i in range(1, n+1):
        dp[i] = max(array[i-1][2] + dp[prev[i-1]], dp[i-1]) 
    return dp[-1]



if __name__ == "__main__":
    array = [
        [1, 4, 5],
        [3, 5, 1],
        [0, 6, 8],
        [4, 7, 4],
        [3, 8, 6],
        [5, 9, 3],
        [6, 10, 2],
        [8, 11, 4]
    ]
    print(MaxProfit(array))