


"""
    给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 对两个普通的字符串进行比较
        # if len(s) != len(p): return False
        # for i in range(len(p)):
        #     if s[i] != p[i]: return False
        # return True

        # 改写成递归形式
        # if not p: return not s
        # first_match = s and p[0] == s[0]
        # return first_match and self.isMatch(s[1: ], p[1: ])

        # 实现"."通配符，代表匹配任意单个字母
        # if not p: return not s
        # first_match = s and p[0] in [s[0], "."]
        # return first_match and self.isMatch(s[1: ], p[1: ])

        # 实现"*"通配符，代表匹配零个或多个字母，但前提是前面必须有一个字母
        if not p: return not s
        first_match = bool(s) and p[0] in [s[0], "."]
        if len(p) >= 2 and p[1] == "*":
            # 找到了"*"号
            return self.isMatch(s, p[2: ]) or first_match and self.isMatch(s[1: ], p)
        else:
            return first_match and self.isMatch(s[1: ], p[1: ])

    def isMatch_1(self, s: str, p: str) -> bool:
        """带备忘录的递归
        """
        if not p: return not s
        memo = dict()
        def dp(i, j):
            # i,j表示s和p当前匹配到的位置
            if (i, j) in memo: return memo[(i, j)]
            if j == len(p): return i == len(s)
            first_match = i < len(s) and p[j] in [s[i], "."]
            if j <= len(p) - 2 and p[j + 1] == "*":
                ans = dp(i, j+2) or first_match and dp(i+1, j)
            else:
                ans = first_match and dp(i+1, j+1)
            memo[(i, j)] = ans
            return ans
        return dp(0, 0)


if __name__ == "__main__":
    ss = Solution()
    s = "aa"
    p = "a*"
    print(ss.isMatch_1(s, p))