#import sys
#sys.stdin = open('input.txt')

from collections import deque

V, E = map(int, input().split())
info = list(map(int, input().split()))
graph = [[] for _ in range(V+1)]
visited = [0]*(V+1)

for i in range(0, len(info), 2):
    graph[info[i]].append(info[i+1])

print(f'#1', end=' ')
def bfs(start, graph, visited):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if visited[i] == 0 and i != 0:
                q.append(i)
                visited[i] = 1

bfs(1, graph, visited)
