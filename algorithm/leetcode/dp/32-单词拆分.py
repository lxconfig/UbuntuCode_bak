
"""
"""

from typing import List
import functools

"""
    不管是动态规划还是DFS回溯，思路都是：
        从索引0的位置开始遍历，每次分割出s[0], s[0..1], s[0..2]....
        对于分割出来的字符串判断一下是否在wordDict中，如果在，则判断剩余部分是否也在
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s: return True
        size = len(s)
        dp = [False for _ in range(size + 1)]
        dp[0] = True
        for i in range(size):
            for j in range(i + 1, size + 1):
                # 因为是要完全分割出来wordDict中的单词
                # 所以要判断一下前面s[: i]是否是匹配上的
                if dp[i] and s[i: j] in wordDict:
                    dp[j] = True
        return dp[size]


    def wordBreak_1(self, s: str, wordDict: List[str]) -> bool:
        # DFS回溯
        if not s: return True
        size = len(s)
        # 这个装饰器的作用就是备忘录
        @functools.lru_cache()
        def dfs(start):
            # 当指针到s的最末端，说明已经全部遍历比较过了
            if start == size:
                return True
            for i in range(start + 1, size + 1):
                # 分割出前面的部分
                prefix = s[start: i]
                # 如果这部分在wordDict中，则递归判断后面的部分
                # 比如分割出leet,就还要判断code是否在wordDict中
                if prefix in wordDict and dfs(i):
                    return True
            return False
        return dfs(0)

    def wordBreak_2(self, s: str, wordDict: List[str]) -> bool:
        if not s: return True
        size, memo = len(s), dict()
        def dfs(start):
            # 当指针到s的最末端，说明已经全部遍历比较过了
            if start == size:
                return True
            if memo[start]: return memo[start]
            for i in range(start + 1, size + 1):
                # 分割出前面的部分
                prefix = s[start: i]
                # 如果这部分在wordDict中，则递归判断后面的部分
                # 比如分割出leet,就还要判断code是否在wordDict中
                if prefix in wordDict and dfs(i):
                    memo[start] = True
                    return True
            memo[start] = False
            return False
        return dfs(0)