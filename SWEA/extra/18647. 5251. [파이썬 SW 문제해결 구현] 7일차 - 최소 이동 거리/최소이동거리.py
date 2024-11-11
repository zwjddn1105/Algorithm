#import sys
import heapq
#sys.stdin = open('5251_input.txt')

INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n, e = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    distance = [INF] * (n+1)
    distance[0] = 0

    dijkstra(0)
    result = distance[n]
    print(f'#{tc} {result}')