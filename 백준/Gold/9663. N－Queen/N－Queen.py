n = int(input())
visited = [[0]*n for _ in range(n)]
cnt = 0

def check(row, col):
    # 같은 열 검사
    for i in range(row):
        if visited[i][col] == 1:
            return False

    # 왼쪽 대각선 위 검사
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if visited[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # 오른쪽 대각선 위 검사
    i = row - 1
    j = col + 1
    while i >= 0 and j < n:
        if visited[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def dfs(row):
    global cnt
    if row == n:
        cnt += 1
        return

    for col in range(n):
        if check(row, col):
            visited[row][col] = 1
            dfs(row+1)
            visited[row][col] = 0

dfs(0)
print(cnt)