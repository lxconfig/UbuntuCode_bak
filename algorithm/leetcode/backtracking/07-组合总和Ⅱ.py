

"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

"""


from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """减法思维
        """
        size, res, path = len(candidates), [], []
        candidates.sort()
        def dfs(candidates, begin, target, res, path):
            # 终止条件
            if target == 0:
                res.append(path[:])
                return 
            for i in range(begin, size):
                if candidates[i] > target:
                    break
                if i > begin and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                dfs(candidates, i+1, target - candidates[i], res, path)
                path.pop()
        dfs(candidates, 0, target, res, path)
        return res

    def combinationSum2_1(self, candidates: List[int], target: int) -> List[List[int]]:
        """加法思维
        """
        size, count, res, path = len(candidates), 0, [], []
        candidates.sort()
        def dfs(candidates, begin, count, res, path):
            if count == target:
                res.append(path[:])
                return
            for i in range(begin, size):
                if candidates[i] > target:
                    break
                if candidates[i] + count > target:
                    continue
                if i > begin and candidates[i] == candidates[i - 1]:
                    continue
                # 做选择
                path.append(candidates[i])
                # 回溯
                dfs(candidates, i+1, sum(path), res, path)
                # 撤销
                count -= candidates[i]
                path.pop()
        
        dfs(candidates, 0, count, res, path)
        return res


if __name__ == "__main__":
    s = Solution()
    candidates, target = [10,1,2,7,6,1,5], 8
    print(s.combinationSum2(candidates, target))