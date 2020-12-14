
def DFS(node):
    graph = {
        "a": ["b", "c", "d"],
        "b": ["a", "e"],
        "c": ["a", "d", "f"],
        "d": ["a", "c", "f"],
        "e": ["b", "f"],
        "f": ["c", "d", "e"]
    }
    # DFS用栈来实现
    stack = []

    seen = []
    stack.append(node)
    seen.append(node)

    while len(stack) != 0:
        # 每次弹出最后一个元素
        vertex = stack.pop()
        nodes = graph[vertex]
        for i in nodes:
            if i not in seen:
                stack.append(i)
                seen.append(i)
        print(vertex, end=" ")



if __name__ == "__main__":
    DFS("a")