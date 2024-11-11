#import sys
from collections import deque
#sys.stdin = open('5105_input.txt')


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    start_x = 0
    start_y = 0
    arrive_x = 0
    arrive_y = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                start_x = i
                start_y = j
            if arr[i][j] == 3:
                arr[i][j] = -1
                arrive_x = i
                arrive_y = j

    q = deque()
    q.append([start_x, start_y])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    arrive = False

    while q:
        v = q.popleft()
        for k in range(4):
            nx = v[0] + dx[k]
            ny = v[1] + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 0:
                    q.append([nx, ny])
                    arr[nx][ny] = arr[v[0]][v[1]] + 1
                elif arr[nx][ny] == -1 :
                    arr[nx][ny] = arr[v[0]][v[1]] + 1
                    arrive = True
                    break
        if arrive:
            break

    result = arr[arrive_x][arrive_y] - 3

    if arrive:
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} 0')
