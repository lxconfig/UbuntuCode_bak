

"""
    Dijkstra算法，找最短路径
"""

import heapq
import sys


graph = {
        "a": {"b": 3, "c": 2, "d": 6},
        "b": {"a": 3, "e": 8},
        "c": {"a": 2, "d": 4, "f": 3},
        "d": {"a": 6, "c": 4, "f": 9},
        "e": {"b": 8, "f": 10},
        "f": {"c": 3, "d": 9, "e": 10}
}


def init_distance(graph, start):
    distance = {start: 0}
    for vertex in graph:
        if vertex != start:
            distance[vertex] = sys.maxsize
    return distance


def dijkstra(graph, start):
    pqueue = []
    visited = set()
    path = {start: None}
    heapq.heappush(pqueue, (0, start))
    distance = init_distance(graph, start)

    while pqueue:
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        visited.add(vertex)
        for vertxin in graph[vertex].keys():
            if vertxin not in visited:
                if dist + graph[vertex][vertxin] < distance[vertxin]:
                    heapq.heappush(pqueue, (dist + graph[vertex][vertxin], vertxin))
                    path[vertxin] = vertex
                    distance[vertxin] = dist + graph[vertex][vertxin]
    return path, distance

if __name__ == "__main__":
    path, distance = dijkstra(graph, "a")
    print(path)
    print(distance)
    
    end = "f"
    while end:
        print(end, end=" ")
        end = path[end]