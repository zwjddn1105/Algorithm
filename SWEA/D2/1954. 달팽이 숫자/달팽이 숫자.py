# import sys
# sys.stdin = open('input.txt')
 
# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
 
    i = 0
    j = 0
    dx = [0, 1, 0, -1] # 행
    dy = [1, 0, -1, 0] # 렬
    direction = 0
 
    number = 1
    while number <= N**2:
        try:
            if arr[i][j] == 0:
                arr[i][j] = number
                i += dx[direction]
                j += dy[direction]
 
            elif arr[i][j] != 0:
                i -= dx[direction]
                j -= dy[direction]
                direction=(direction+1)%4
                i += dx[direction]
                j += dy[direction]
                arr[i][j] = number
                i += dx[direction]
                j += dy[direction]
        except IndexError:
            i -= dx[direction]
            j -= dy[direction]
            direction=(direction+1)%4
            i += dx[direction]
            j += dy[direction]
            arr[i][j] = number
            i += dx[direction]
            j += dy[direction]
        finally:
            number += 1
 
 
    print(f'#{tc}')
    for q in range(N):
        print(*arr[q])