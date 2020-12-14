
"""
"""


from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        size = len(s)
        if size > 12 or size < 4: return []
        res, path, begin, ip_times = [], [], 0, 0
        def dfs(s, begin, ip_times, res, path):
            """
            s: 原字符串
            begin: 表示开始分割(选择)的起始位置，初始值为0，表示从第一个字符开始选择
            ip_times: 表示当前已经分割出几段ip的子地址，如：192.168.xx.xxx, 此时 ip_times = 2
            res: 结果集
            path: 路径，表示某个合法的ip地址
            """
            # 终止条件，表示已经分割到最后了
            if begin == size:
                # 当有4段子地址时，借结束
                if ip_times == 4:
                    res.append(".".join(path[:]))
                    return 
            # 剩下的位数太多 或 太少
            if size - begin > 3 * (4 - ip_times) or size - begin < (4 - ip_times):
                return 
            # 表示选1位数，2位数，3位数
            for i in range(3):
                if begin + i >= size:
                    break
                # 判断选择是否有效
                if not isValid(s, begin, begin + i):
                    continue
                # 选择
                path.append(s[begin: begin + i + 1])
                # 回溯
                dfs(s, begin + i + 1, ip_times + 1, res, path)
                # 撤销选择
                path.pop()
        def isValid(s, left, right):
            """
            s: 原字符串
            left: 开始分割的左边界
            right: 开始分割的右边界
            """
            size = right - left + 1
            if size > 1 and s[left] == "0":
                return False
            tmp = int(s[left: right + 1])
            if tmp > 255: 
                return False
            return True
        
        dfs(s, begin, ip_times, res, path)
        return res