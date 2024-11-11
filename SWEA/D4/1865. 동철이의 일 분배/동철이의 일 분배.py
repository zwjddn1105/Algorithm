T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr[i][j] /= 100

    max_probability = 0  # 최대 확률을 저장할 변수
    visited = [0] * n

    def dfs(row, result):
        global max_probability
        if row == n:
            max_probability = max(max_probability, result)
            return

        if result <= max_probability:
            return

        for col in range(n):
            if not visited[col]:
                visited[col] = True
                dfs(row + 1, result * arr[row][col])
                visited[col] = False

    dfs(0, 1)  
    max_probability *= 100
    print(f'#{tc} {max_probability:.6f}')