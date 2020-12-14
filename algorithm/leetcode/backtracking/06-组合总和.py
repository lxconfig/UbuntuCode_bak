
"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中可以无限次使用。
"""


from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """减法思维，从target开始一点一点减到0，小于0则返回
        """
        size, res, path, begin = len(candidates), [], [], 0
        
        def dfs(candidates, begin, target, res, path):
            # 终止条件
            if target < 0: return 
            if target == 0:
                res.append(path[:])
                return 
            for i in range(begin, size):
                # 做选择
                path.append(candidates[i])
                # 回溯
                dfs(candidates, i, target - candidates[i], res, path)
                # 撤销选择
                path.pop()
        dfs(candidates, begin, target, res, path)
        return res

    def combinationSum_1(self, candidates: List[int], target: int) -> List[List[int]]:
        """加法思维，从0开始加，直到加到target，若是超过则返回
        """
        size, res, count, path, begin = len(candidates), [], 0, [], 0
        def dfs(candidates, begin, count, target, res, path):
            if count == target:
                res.append(path[:])
                return 
            for i in range(begin, size):
                if count + candidates[i] > target:
                    # 这里若是写break则数组需要排序，因为只有排序了，才能确定之后的数字肯定加起来也是大于target的
                    # 而continue则只是能知道当前这个candidates[i]不合适，之后的数字没法断定
                    continue
                path.append(candidates[i])
                dfs(candidates, i, sum(path), target, res, path)
                count -= candidates[i]
                path.pop()
        dfs(candidates, begin, count, target, res, path)
        return res

if __name__ == "__main__":
    s = Solution()
    candidates, target = [2,3,6,7], 7
    print(s.combinationSum_1(candidates, target))