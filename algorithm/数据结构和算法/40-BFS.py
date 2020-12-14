

def BFS(start):
    """广度优先搜索
    start: 开始顶点
    """
    graph = {
        "a": ["b", "c", "d"],
        "b": ["a", "e"],
        "c": ["a", "d", "f"],
        "d": ["a", "c", "f"],
        "e": ["b", "f"],
        "f": ["c", "d", "e"]
    }
    if not graph.get(start):
        print(None)
        return 
    queue = []
    visited = set(start)
    path = {start: None}
    queue.append(start)
    # visited.add(start)

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=" ")
        for vertxin in graph[vertex]:
            if vertxin not in visited:
                queue.append(vertxin)
                visited.add(vertxin)
                path[vertxin] = vertex
    return path


if __name__ == "__main__":
    path = BFS("a")
    print()
    print(path)