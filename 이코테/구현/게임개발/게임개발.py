n, m = map(int, input().split())

start_x, start_y, direction = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

visited[start_x][start_y] = 1
count = 1
turn_time = 0
while True:
    turn_left()
    nx = start_x + dx[direction]
    ny = start_y + dy[direction]
    if visited[nx][ny] == 0 and 0<=nx<n and 0<=ny<m and arr[nx][ny] == 0:
        visited[nx][ny] = 1
        count += 1
        start_x = nx
        start_y = ny
        turn_time = 0
        continue
    else:
        turn_time += 1
        if turn_time == 4:
            nx = start_x - dx[direction]
            ny = start_y - dy[direction]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or arr[nx][ny] == 1:
                break
            else:
                start_x = nx
                start_y = ny
                turn_time = 0
print(count)