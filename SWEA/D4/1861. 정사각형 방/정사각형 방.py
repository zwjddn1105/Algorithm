#import sys

#sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    v = [0]*(n**2 + 1)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(n):
        for j in range(n):
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0<=ni<n and 0<=nj<n:
                    if arr[ni][nj] == arr[i][j] + 1:
                        v[arr[i][j]] = 1
                        break
    cnt = 0
    max_cnt = 0
    start = 0

    for i in range(n**2, -1, -1):
        if v[i]:
            cnt += 1
        else:
            if max_cnt <= cnt:
                max_cnt = cnt
                start = i + 1
            cnt = 0

    print(f'#{tc} {start} {max_cnt + 1}')
