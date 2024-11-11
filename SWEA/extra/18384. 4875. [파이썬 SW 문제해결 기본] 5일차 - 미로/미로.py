#import sys

#sys.stdin = open('4875_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input().strip())
    arr = [list(map(int, input().strip())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                x1, y1 = i, j
            if arr[i][j] == 3:
                x2, y2 = i, j

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def back_tracking(x, y, visited):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    back_tracking(nx, ny, visited)
                elif arr[nx][ny] == 3 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    return

    visited[x1][y1] = 1
    back_tracking(x1, y1, visited)

    if visited[x2][y2] == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
