# 토마토 풍년!
from collections import deque

m,n,h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]


q = deque()
day = 0 # while문에서 첫날에도 day가 1 더해지므로

# 덱 안에 우선 토마토 위치 넣기, 토마토 값 빈 리스트에 넣기
for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[k][i][j] == 1:
                q.append([k, i, j])

while q: # 큐가 비게되면 영향을 끼치는 토마토 위치가 더이상 없음
    one_day = len(q) 

    dx = [0, 0, 1, -1, 0, 0]    
    dy = [1, -1, 0, 0, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    for _ in range(one_day):
        z, x, y = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nz<h and 0<=nx<n and 0<=ny<m and tomato[nz][nx][ny] == 0: # 토마토 빈 곳은 무시
                tomato[nz][nx][ny] = 1
                q.append([nz, nx, ny])   
    day += 1

def remain_nomat_tomato():
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if tomato[k][i][j] == 0: # 안 익은 토마토가 남아있다면
                    return 0
    return 1
                
if remain_nomat_tomato():
    print(day-1)
else:
    print(-1)
