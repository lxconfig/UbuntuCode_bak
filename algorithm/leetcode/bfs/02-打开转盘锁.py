
"""
"""


from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def plusUp(node, index):
            # 由于是四个字符组成的密码，index表示扭动的是第几个字符
            tmp_list = [i for i in node]
            if tmp_list[index] == "9":
                tmp_list[index] = "0"
            else:
                tmp_list[index] = str(int(tmp_list[index]) + 1)
            return "".join(tmp_list)
        
        def plusDown(node, index):
            tmp_list = [i for i in node]
            if tmp_list[index] == "0":
                tmp_list[index] = "9"
            else:
                tmp_list[index] = str(int(tmp_list[index]) - 1)
            return "".join(tmp_list)

        queue, step, visited = [], 0, set()
        queue.append("0000")
        visited.add("0000")
        while queue:
            size = len(queue)
            for _ in range(size):
                cur_node = queue.pop(0)
                if cur_node in deadends:
                    continue
                # 判断是否等于终点target
                if cur_node == target:
                    return step
                # 将节点的邻居节点加入队列
                for i in range(4):
                    # 可以向上扭动
                    up = plusUp(cur_node, i)
                    if up not in visited:
                        queue.append(up)
                        visited.add(up)
                    # 也可以向下扭动
                    down = plusDown(cur_node, i)
                    if down not in visited:
                        queue.append(down)
                        visited.add(down)
            step += 1
        return -1

    def openLock_1(self, deadends: List[str], target: str) -> int:
        """双向BFS优化
        """
        def plusUp(node, index):
            # 由于是四个字符组成的密码，index表示扭动的是第几个字符
            tmp_list = [i for i in node]
            if tmp_list[index] == "9":
                tmp_list[index] = "0"
            else:
                tmp_list[index] = str(int(tmp_list[index]) + 1)
            return "".join(tmp_list)
        
        def plusDown(node, index):
            tmp_list = [i for i in node]
            if tmp_list[index] == "0":
                tmp_list[index] = "9"
            else:
                tmp_list[index] = str(int(tmp_list[index]) - 1)
            return "".join(tmp_list)

        queue1, queue2, step, visited = [], [], 0, set()
        queue1.append("0000")
        queue2.append(target)
        while queue1 and queue2:
            temp = set()
            for node in queue1:
                if node in deadends:
                    continue
                if node in queue2:
                    return step
                visited.add(node)
                # 将节点的邻居节点加入队列
                for i in range(4):
                    # 可以向上扭动
                    up = plusUp(node, i)
                    if up not in visited:
                        temp.add(up)
                    # 也可以向下扭动
                    down = plusDown(node, i)
                    if down not in visited:
                        temp.add(down)
            step += 1
            queue1 = queue2
            queue2 = temp
        return -1

if __name__ == "__main__":
    s = Solution()
    deadends = ["0000"]
    target = "8888"
    print(s.openLock_1(deadends, target))