

def DFS(start):
    """深度优先搜索(循环实现)
    start: 起始顶点
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
    stack = []
    visited = set()
    path = {start: None}
    stack.append(start)
    visited.add(start)

    while stack:
        vertex = stack.pop()
        print(vertex, end=" ")
        for vertxin in graph[vertex]:
            if vertxin not in visited:
                stack.append(vertxin)
                visited.add(vertxin)
                path[vertxin] = vertex
    return path


def DFS_Recursive(start):
    """深度优先搜索(递归版)
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
    visited = set()
    visited.add(start)
    print(start, end=" ")
    for vertex in graph[start]:
        if vertex not in visited:
            helper(graph, vertex, visited)

def helper(graph, vertex, visited):
    visited.add(vertex)
    print(vertex, end=" ")
    for vertex in graph[vertex]:
        if vertex not in visited:
            helper(graph, vertex, visited)
    


if __name__ == "__main__":
    path = DFS("a")
    print()
    # DFS_Recursive("a")
    print(path)