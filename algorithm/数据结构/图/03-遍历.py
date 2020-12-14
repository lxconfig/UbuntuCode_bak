
graph = {
        "a": ["b", "c", "d"],
        "b": ["a", "e"],
        "c": ["a", "d", "f"],
        "d": ["a", "c", "f"],
        "e": ["b", "f"],
        "f": ["c", "d", "e"]
}

def DFS(graph, start):
    """深度优先搜索
    """
    stack = [start]
    visited = set()
    visited.add(start)
    path = {start: None}

    while stack:
        vertex = stack.pop()
        print(vertex, end=" ")
        for vertxin in graph[vertex]:
            if vertxin not in visited:
                stack.append(vertxin)
                visited.add(vertxin)
                path[vertxin] = vertex
    return path


def BFS(graph, start):
    """广度优先搜索
    """
    queue, visited, path = [start], {start}, {start: None}
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
    print(DFS(graph, "a"))
    print()
    print(BFS(graph, "a"))