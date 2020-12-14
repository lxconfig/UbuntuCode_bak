

def BFS(node):
    """BFS: 广度优先遍历"""
    # 用队列实现广度优先遍历
    queue = []

    # 保存每个节点的邻接点
    graph = {
        "a": ["b", "c"],
        "b": ["a", "c", "d"],
        "c": ["a", "b", "d", "e"],
        "d": ["b", "c", "e", "f"],
        "e": ["c", "d"],
        "f": ["d"]
    }

    # BFS可以用来计算从某个点到某个点的最短路径
    parent = {node: None}   # 记录每个点前一个点是什么，node由于是开始的点，所以没有前一个点

    # 先将一个节点放到队列中
    queue.append(node)
    # 已经遍历过的，放到seen中
    seen = []
    seen.append(node)

    # 然后将他的邻接点依次放到队列中
    while len(queue) != 0:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for i in nodes:
            if i not in seen:
                queue.append(i)
                seen.append(i)
                parent[i] = vertex  # 每个邻接点i的前一个点是vertex
        # print(vertex, end=" ")
    return parent


if __name__ == "__main__":
    parent = BFS("a")
    print(parent)
    end = "d"
    while end != None:
        print(end)
        end = parent[end]