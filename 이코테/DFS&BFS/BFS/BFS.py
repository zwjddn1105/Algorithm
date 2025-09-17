# BFS가 DFS보다 더 빠르게 동작한다는 점만 기억하자
# 얘도 시간복잡도는 O(N)
from collections import deque
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

def bfs(graph, start, visited):
    visited[start] = 1
    queue = deque([start])
    # queue.append(start)
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
# 노드 8개
visited = [0] * 9

bfs(graph, 1, visited) # 1 2 3 8 7 4 5 6
