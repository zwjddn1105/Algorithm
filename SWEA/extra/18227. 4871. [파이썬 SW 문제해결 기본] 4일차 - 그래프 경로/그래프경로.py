#import sys

#sys.stdin = open('4871_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    V, E = map(int, input().split())
    visited = [False] * (V+1)
    graph = [[] for _ in range(V+1)]

    for i in range(E):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[x].sort()

    S, G = map(int, input().split())
    result = []
    answer = 0

    def dfs(start):
        visited[start] = True
        stack = [start]
        result.append(start)
        while True:
            for w in graph[start]:
                if not visited[w]:
                    stack.append(w)
                    result.append(w)
                    visited[w] = True
                    start = w
                    break
            else:
                if stack:
                    stack.pop()
                    if stack:
                        start = stack[-1]
                    else:
                        break

    dfs(S)

    if S in result and G in result:
        answer = 1
    else:
        answer = 0

    print(f'#{tc} {answer}')