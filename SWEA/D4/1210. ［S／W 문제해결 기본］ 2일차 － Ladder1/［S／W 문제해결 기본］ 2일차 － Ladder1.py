# import sys
# sys.stdin = open('input.txt')
 
# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    dx = [0, 0, -1]
    dy = [-1, 1, 0]
    i = 99
 
    for u in range(100):
        if arr[99][u] == 2:
            j = u
 
    while i > 0:
        for k in range(3):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < 100 and 0 <= ny < 100:
                if arr[nx][ny] == 1:
                    i = nx
                    j = ny
                    arr[nx][ny] = 0
 
    print(f'#{tc} {j}')