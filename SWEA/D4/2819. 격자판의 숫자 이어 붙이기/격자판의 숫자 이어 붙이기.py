#import sys

#sys.stdin = open('sample_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    arr = [list(map(str, input().split())) for _ in range(4)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    result = ''

    lst = set()
    def dfs(i, j, result):
        if len(result) == 7:
            lst.add(result)
            return
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0<=nx<4 and 0<=ny<4:
               dfs(nx, ny, result + arr[nx][ny])

    for i in range(4):
        for j in range(4):
            dfs(i, j, result)

    print(f'#{tc} {len(lst)}')