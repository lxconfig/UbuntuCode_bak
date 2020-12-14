
"""
    请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 
    在本题中，匹配是指字符串的所有字符匹配整个模式。
    例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配


    思路1：分清各种情况
        1. str和pattern都是空时，返回True
        2. 经过匹配后，当pattern为空，而str不为空时，直接返回False
           2.1. 注意，当str为空，但是pattern不为空，是可能匹配成功的，考虑这种情况：str=aaa  parttern=aa.b*
        3. 关于pattern包含'*'字符
            3.1 '*'字符匹配0个字符时，当前str字符不变，parttern字符往后移两个，跳过'*'字符
            3.2 '*'字符匹配1个或多个字符时，当前str字符往后移一个，pattern字符不变
                一个字符和多个字符可以看作一种情况，因为当匹配到一个时，str后移一个，pattern不变，就变成3.1的情况
                多个字符会转变为一个字符，一个字符会转变为0个字符
"""

import pysnooper


class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        """递归回溯
        """
        # 运行时间：25ms  占用内存：5752k
        # 第1.种情况
        if not s and not pattern:
            return True
        # 第2.种情况
        if s and not pattern:
            return False
        # 第2.1种情况
        if not s and pattern:
            if len(pattern) > 1 and pattern[1] == "*":
                return self.match(s, pattern[2:])
            else:
                # 只有包含'*'字符才可能匹配成功
                return False
        # s和pattern都不为空时
        # pattern[1]='*'时
        if len(pattern) > 1 and pattern[1] == '*':
            if s[0] != pattern[0] and pattern[0] != '.':
                # 还要继续比较，因为pattern[1]='*'
                return self.match(s, pattern[2:])
            else:
                # 如果s[0]=pattern[0]，且pattern[1]='*'，就可能匹配0个、1个、多个
                # return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)
                return self.match(s, pattern[2:]) or self.match(s[1:], pattern)
        else:
            # pattern[1] != '*'时
            if s[0] == pattern[0] or pattern[0] == '.':
                return self.match(s[1:], pattern[1:])
            else:
                return False

    # @pysnooper.snoop()
    def match2(self, s, pattern):
        """动态规划
            定义状态 i 和 j，分别表示 s中前i个字符和pattern中前j个字符是否匹配，就是求dp[i][j]
            假设已知 dp[i-1][j-1]，根据目前的s[i] 和 pattern[j]，求出dp[i][j]
            初始状态中：dp[0][0] = True
            1. s[i] == pattern[j] or pattern[j] == '.'
                此时由于两个元素能匹配上，所以 dp[i][j] = dp[i-1][j-1]

            2. pattern[j] == '*'
                有'*'字符时，要比较的是前一个字符即j-1。

            2.1 s[i] != pattern[j-1]
                此时，由于两个元素不匹配，并且包含'*'字符
                只能把'*'字符和它前面的字符看作不存在，跳过它们两个。所以 dp[i][j] = dp[i][j-2]

            2.2 s[i] == pattern[j-1] or pattern[j-1] == '.'
                此时会有两种情况：
                    2.2.1 '*'匹配0个字符。也只能把'*'字符和前面的字符看作不存在。所以 dp[i][j] = dp[i][j-2]
                    2.2.2 '*'匹配1个或多个字符。只需要找下一个字符继续匹配即可。所以 dp[i][j] = dp[i-1][j]
            
            总结：
                              dp[i-1][j-1]               s[i] == pattern[j] or pattern == '.'               
                dp[i][j] =    dp[i][j-2]                 pattern[j] == '*', s[i] != pattern[j-1]
                              dp[i][j-2] or dp[i-1][j]   pattern[j] == '*', s[i] == pattern[j-1] or pattern[j] == '.'

        """
        # 运行时间：25ms  占用内存：5804k
        if not s and not pattern:
            return True
        if s and not pattern:
            # s有值，但pattern为空，一定是Fasle
            return False

        m, n = len(s)+1, len(pattern)+1
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True

        # if not s and len(pattern) > 1:
            # s为空，但pattern有值，此时需要判断，因为可能有'*'字符存在
            # dp[0][j] = dp[0][j-2]
        for j in range(2, n):
            if pattern[j-1] == "*":
                dp[0][j] = dp[0][j-2]
            else:
                dp[0][j] = False
        
        for k in range(1, m):
            i = k - 1
            for z in range(1, n):
                j = z - 1
                if s[i] == pattern[j] or pattern[j] == ".":
                    dp[k][z] = dp[k-1][z-1]
                elif pattern[j] == "*":
                    if s[i] == pattern[j-1] or pattern[j-1] == ".":
                        dp[k][z] = dp[k][z-2] or dp[k-1][z]
                    else:
                        dp[k][z] = dp[k][z-2]
                else:
                    # 比如 s = a   pattern = c，不满足上面的条件
                    dp[k][z] = False
        return dp


if __name__ == "__main__":
    solution = Solution()
    s = "aa"
    pattern = ".*"
    print(solution.match(s, pattern))