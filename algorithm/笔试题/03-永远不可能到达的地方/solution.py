
def helper(graph, s, t):
    stack = []
    seen = []
    ret = []
    stack.append(s)
    seen.append(s)

    while len(stack) != 0:
        vertex = stack.pop()
        ret.append(vertex)
        if vertex == t:
            return ret
        if graph[vertex] not in seen:
            stack.append(graph[vertex])
            seen.append(graph[vertex])
    return ret


while True:
    params = list(map(int, input().split(' ')))
    n, m = params[0], params[1]
    ab = []
    for i in range(m):
        ab.append(list(map(int, input().split(' '))))
        # helper(a, b)
    st = list(map(int, input().split(' ')))
    s, t = st[0], st[1]
    temp = []
    ret = helper(dict(ab), s, t)
    for i in ab:
        for j in i:
            if j not in temp:
                temp.append(j)
    
    for i in list(set(temp).difference(set(ret))):
        print(i, end=" ")







