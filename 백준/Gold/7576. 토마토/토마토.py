from collections import deque
m, n = map(int, input().split())

tomatos = []
q = deque()
answer = 0

for _ in range(n):
    tomato = list(map(int, input().split()))
    tomatos.append(tomato)


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs():
    global answer
    while q:
        i, j, day = q.popleft()
        answer = day
  
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0<=nx<n and 0<=ny<m and tomatos[nx][ny] == 0:
                q.append([nx, ny, day+1])
                tomatos[nx][ny] = 1

for i in range(n):
    for j in range(m):
        if tomatos[i][j] == 1:
            q.append([i, j, 0])

bfs()

for i in range(n):
    for j in range(m):
        if tomatos[i][j] == 0:
            answer = -1
            break

print(answer)