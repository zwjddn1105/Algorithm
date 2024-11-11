#import sys

#sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(16)]

    start_x = 0
    start_y = 0
    arrive_x = 0
    arrive_y = 0

    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                start_x = i
                start_y = j
            if arr[i][j] == 3:
                arrive_x = i
                arrive_y = j


    def road(a, b):
        global arr
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]
            if 0 <= nx < 16 and 0 <= ny < 16:
                if arr[nx][ny] == 0 or arr[nx][ny] == 3:
                    arr[nx][ny] = 2
                    road(nx, ny)

    road(start_x, start_y)

    if arr[arrive_x][arrive_y] == 2:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')