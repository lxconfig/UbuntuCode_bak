

"""
    一条包含字母 A-Z 的消息通过以下方式进行了编码：
    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26
    给定一个只包含数字的非空字符串，请计算解码方法的总数。
"""

# import pysnooper



class Solution:
    # @pysnooper.snoop()
    def numDecodings(self, s: str) -> int:
        """动态规划
        爬楼梯的思想
        因为每次要么解码一个字母要么解码两个字母，本题中解码的字母都是数字形式的字符串
            dp[i] = dp[i-1] + dp[i-2]
        但是需要考虑边界条件：
            划分出来的一个数字，可能是无效的(等于0)
            划分出来的两个数字，可能是无效的(不在[10-26]范围内)            
        """
        if not s or s == "0" or s[0] == "0": return 0
        n, dp = len(s), [1, 1]
        if n == 1: return 1
        for i in range(2, n+1):
            ret = 0
            # 划分两个数字串
            if 10 <= int(s[i-2: i]) <= 26:
                ret += dp[i-2]
            # 划分一个数字串
            if s[i-1] != "0":
                ret += dp[i-1]
            dp.append(ret)
        return dp[n]


if __name__ == "__main__":
    s = Solution()
    print(s.numDecodings("01"))