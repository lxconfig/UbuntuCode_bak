

"""
    有一个楼梯，每次可以走1层或2层，cost数组表示每一层所需要的花费。计算登顶的最少花费
"""
# import pysnooper

# @pysnooper.snoop()

def MinCost(cost):
    # O(n)  time
    # O(n)  space

    n = len(cost)
    if n == 0:
        return None
    elif n == 1:
        return cost[0]
    dp = [0] * n
    dp[0], dp[1] = cost[0], cost[1]

    for i in range(2, n):
        dp[i] = min(dp[i-1]+cost[i], dp[i-2]+cost[i])
    
    return dp[n-1]



if __name__ == "__main__":
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(MinCost(cost))