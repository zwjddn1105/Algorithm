#import sys

#sys.stdin = open('sample_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    shave = False
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    highest = 0
    longest = 0

    def dfs(i, j, path):
        global longest, shave
        for l in range(4):
            nx = i + dx[l]
            ny = j + dy[l]
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                if arr[nx][ny] < arr[i][j]:
                    visited.append((nx, ny))
                    dfs(nx, ny, path+1)
                    visited.pop()
                else:
                    if not shave:
                        shave = True
                        q = 1
                        while q <= k:
                            if arr[nx][ny] - q < arr[i][j] and (nx, ny) not in visited:
                                arr[nx][ny] -= q
                                visited.append((nx, ny))
                                dfs(nx, ny, path+1)
                                visited.pop()
                                arr[nx][ny] += q
                            q += 1
                        shave = False
        if path > longest:
            longest = path

    for i in range(n):
        for j in range(n):
            if arr[i][j] > highest:
                highest = arr[i][j]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == highest:
                visited = [(i, j)]
                dfs(i, j, 1)


    print(f'#{tc} {longest}')