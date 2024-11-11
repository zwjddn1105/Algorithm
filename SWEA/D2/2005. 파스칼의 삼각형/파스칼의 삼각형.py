#import sys

#sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]

    for i in range(n):
        arr[i][0] = 1
    dx =[-1, -1]
    dy =[0, -1]
    for i in range(n):
        for j in range(1, n):
            for k in range(2):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0<= nx <n and 0<=ny<n:
                    arr[i][j] += arr[nx][ny]

    print(f'#{tc}')
    for i in range(n):
        for j in range(n):
            if arr[i][j] == False:
                break
            if arr[i][j]:
                print(arr[i][j], end=' ')
        print()