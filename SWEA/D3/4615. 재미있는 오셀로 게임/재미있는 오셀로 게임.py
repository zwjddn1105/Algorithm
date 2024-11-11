#import sys

#sys.stdin = open('sample_input(1).txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [[0]*n for _ in range(n)]
    # 블랙 1 화이트 2
    arr[(n//2)-1][(n//2)-1] = 2
    arr[(n//2)][(n//2)] = 2
    arr[(n//2)][(n//2)-1] = 1
    arr[(n//2)-1][n//2] = 1

    for _ in range(m):
        y, x, color = map(int, input().split())     # x-1, y-1 위치에 놓을 것
        arr[x-1][y-1] = color
        dx = [-1, -1, -1, 0, 1, 1, 1, 0]    # 좌상단부터 시계방향
        dy = [-1, 0, 1, 1, 1, 0, -1, -1]
        for k in range(8):
            q = 1
            lst = []
            while True:
                nx = x-1 + dx[k]*q
                ny = y-1 + dy[k]*q
                if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != color and arr[nx][ny] != 0:
                    lst.append([nx, ny])
                    q += 1
                    continue
                elif 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == color and arr[nx][ny] != 0:
                    if lst:
                        for i in lst:
                            arr[i[0]][i[1]] = color
                        break
                    else:
                        break
                elif 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
                    break
                else:
                    break
    black = 0
    white = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                black += 1
            elif arr[i][j] == 2:
                white += 1
    print(f'#{tc} {black} {white}')