#import sys

#sys.stdin = open('input.txt')

# Testcase 수
T = 1
# Testcase 만큼 반복
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0]*(V+1) for _ in range(V+1)]
    visited = [False] * (V+1)          # 시작값이 1이라서

    # 인접행렬 만들기
    info = list(map(int, input().split()))
    for a in range(0, E*2, 2):
        graph[info[a]][info[a+1]] = 1
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j]:
                graph[j][i] = graph[i][j]
            if graph[j][i]:
                graph[i][j] = graph[j][i]

    result = []

    def dfs_hr(start):
        visited[start] = 1
        result.append(str(start))
        for next in range(1, V+1):
            if graph[start][next] == 1 and not visited[next]:
                dfs_hr(next)
    dfs_hr(1)


    print(f'#{tc} ', end='')
    print('-'.join(result))