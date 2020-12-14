
"""
    输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
    输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
"""
import pysnooper


class Solution:

    def Permutation(self, ss):
        # 运行时间：26ms  占用内存：5732k
        if not ss:
            return []
        if len(ss) <= 1:
            return ss
        res = set()
        for i in range(len(ss)):
            for j in self.Permutation(ss[:i] + ss[i+1:]):
                res.add(ss[i] + j)
        return sorted(res)
    

    def Permutation_1(self, ss):
        """仅针对不重复的情况
        """
        if not ss: return []
        root = []
        res = []
        
        # @pysnooper.snoop()
        def backref(ss, res, root):
            if len(root) == len(ss):
                res.append(root[:])
                return 
            for i in ss:
                if i in root: continue
                root.append(i)
                backref(ss, res, root)
                root.remove(i)
        backref(ss, res, root)
        
        res = ["".join(i) for i in res]
        return res
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.Permutation_1("aa"))