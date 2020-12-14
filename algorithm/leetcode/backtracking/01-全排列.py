

"""
    给定一个 没有重复 数字的序列，返回其所有可能的全排列
"""

class Solution:
    def permute(self, nums: list) -> list:
        """针对没有重复元素的全排列
        """
        if not nums: return []
        res, root = [], []

        def backref(nums, res, root):
            if len(root) == len(nums):
                res.append(root[:])
                return 
            for i in nums:
                if i in root: continue
                root.append(i)
                backref(nums, res, root)
                root.remove(i)
        backref(nums, res, root)
        return res
    
    def permute_1(self, nums: list) -> list:
        """和上面的思路基本一致
        """
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                # 结束条件
                res.append(path[:])
                return 
            for i in range(size):
                if not used[i]:
                    # 做选择，used列表用来判断当前元素是否被访问过
                    # 相当于上一个方法的：if i in root: continue
                    used[i] = True
                    path.append(nums[i])
                    # 进入下一层决策树
                    dfs(nums, size, depth+1, path, used, res)
                    # 撤销选择
                    used[i] = False
                    path.pop()

        if not nums: return []
        size, res, path = len(nums), [], []
        used = [False for _ in range(size)]
        dfs(nums, size, 0, path, used, res)
        return res
        
    
    def permute_2(self, nums: list) -> list:
        """针对有重复元素的全排列
        """
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                # 结束条件
                res.append(path[:])
                return 
            for i in range(size):
                if not used[i]:
                    # 剪枝，若当前元素和前一个元素相同，且前一个元素还没有使用的时候，需要剪枝
                    if i > 0 and nums[i] == nums[i-1] and not used[i - 1]:
                        continue
                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, size, depth+1, path, used, res)
                    used[i] = False
                    path.pop()

        if not nums: return []
        nums.sort()   # 需要排序，这样才能配合剪枝的代码
        size, res, path = len(nums), [], []
        used = [False for _ in range(size)]
        dfs(nums, size, 0, path, used, res)
        return res

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3]
    print(s.permute(nums))