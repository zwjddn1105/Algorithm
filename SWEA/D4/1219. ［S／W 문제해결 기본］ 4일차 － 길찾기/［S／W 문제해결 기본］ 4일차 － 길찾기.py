# import sys

# sys.stdin = open('input.txt')

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(100)]
    visited = [0] * 100
    info = list(map(int, input().split()))
    # print(info)
    for a in range(0, m*2, 2):
        graph[info[a]].append(info[a+1])
        graph[info[a]].sort()
    # print(graph)
    def dfs_stack(graph, start):
        stack = [start]
        visited[start] = 1
        while stack:
            v = stack.pop()
            for i in graph[v][::-1]:
                if not visited[i]:
                    stack.append(i)
                    visited[i] = 1

    dfs_stack(graph, 0)

    if visited[99] == 1:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')
