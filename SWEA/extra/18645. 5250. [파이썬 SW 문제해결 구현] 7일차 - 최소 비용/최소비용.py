#import sys
from heapq import heappush, heappop
#sys.stdin = open('5250_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    INF = int(1e9)
    distance = [[INF] * n for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def dijkstra(start_x, start_y):
        q = []
        heappush(q, (0, start_x, start_y))
        distance[start_x][start_y] = 0
        while q:
            dist, i, j = heappop(q)
            if dist > distance[i][j]:
                continue
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0<=nx<n and 0<=ny<n:
                    if graph[i][j] >= graph[nx][ny]:
                        if distance[nx][ny] > dist:
                            distance[nx][ny] = dist + 1
                            heappush(q, (dist+1, nx, ny))
                    else:
                        value = abs(graph[i][j] - graph[nx][ny])
                        if distance[nx][ny] > dist + value + 1:
                            distance[nx][ny] = dist + value + 1
                            heappush(q, (dist+value+1, nx, ny))
    dijkstra(0,0)

    print(f'#{tc} {distance[n-1][n-1]}')