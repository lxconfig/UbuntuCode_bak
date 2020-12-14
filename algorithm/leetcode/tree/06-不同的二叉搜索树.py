

"""
    给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
"""


class Solution:
    def numTrees(self, n: int) -> int:
        """动态规划法
        记dp[i]表示有i个节点时，能组成的二叉搜索树种数
        定义 dp[0] = dp[1] = 1,表示有1种
        第一层循环表示总共有几个节点，第二层循环表示这些节点的范围
        如： n = 3时，i取[2,3]，对应的j取[1,2]或[1,2,3]
        根据卡塔兰数的公式：
            h(n)= h(0)*h(n-1)+h(1)*h(n-2) + ... + h(n-1)*h(0) (n>=2)
        所以状态方程定义为：
            dp[i] += dp[j - 1] * dp[i - j]
        其中：
            dp[j - 1]表示左子树
            dp[i - j]表示右子树
        """
        if n == 0: return 0
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        print(dp)
        return dp[n]


if __name__ == "__main__":
    s = Solution()
    print(s.numTrees(3))