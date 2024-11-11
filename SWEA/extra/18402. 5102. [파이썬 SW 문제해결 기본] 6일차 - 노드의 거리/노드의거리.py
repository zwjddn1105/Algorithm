#import sys

#sys.stdin = open('5102_input.txt')
from collections import deque
# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        graph[a].sort()
        graph[b].sort()
    S, G = map(int, input().split())

    visited = [0] * (V+1)
    queue = deque()
    queue.append([S, 0])
    visited[S] = True
    result = 0
    def bfs(S, G, graph, visited):
        global result
        while queue:
            v = queue.popleft()
            a = v[0]
            b = v[1]
            for i in graph[a]:
                if not visited[i]:
                    queue.append([i, b+1])
                    visited[i] = True
                if i == G:
                    result = b+1
                    break
            if result != 0:
                break

    bfs(S, G, graph, visited)

    print(f'#{tc} {result}')

