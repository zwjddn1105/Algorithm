from collections import deque
n, m = map(int, input().split())
start = [1, 1]
graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()
visited = [[0]*m for _ in range(n)]
def bfs(i, j):
    q.append([i, j])
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        if x == n-1 and y == m-1:
            return 
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])

bfs(0,0)

print(visited[n-1][m-1])




# dfs로하는 백트래킹 코드
# 입력 그래프
graph = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]

# 상, 하, 좌, 우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, depth, visited, graph, min_dist):
    n, m = len(graph), len(graph[0])

    # 목표 지점 도착 시 최단 거리 갱신
    if x == n - 1 and y == m - 1:
        min_dist[0] = min(min_dist[0], depth)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        # 범위 내, 이동 가능(1), 미방문 상태일 때 이동
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = True  # 방문 체크
            dfs(nx, ny, depth + 1, visited, graph, min_dist)
            visited[nx][ny] = False  # 백트래킹

def find_shortest_path_dfs(graph):
    n, m = len(graph), len(graph[0])
    visited = [[False] * m for _ in range(n)]
    min_dist = [float('inf')]  # 최단 거리 저장 (리스트로 전달)

    # 시작점 방문
    visited[0][0] = True
    dfs(0, 0, 1, visited, graph, min_dist)

    return min_dist[0] if min_dist[0] != float('inf') else -1  # 도달 불가능하면 -1

# 실행
result = find_shortest_path_dfs(graph)
print(result)  # 최단 거리 출력
