# DFS 예제
# 인접행렬은 인접리스트방식보다 메모리를 불필요하게 더 낭비하게된다.
# [ [0, 7, 5]
#   [7, 0, INF]
#   [5, INF, 0] ] 이런형태가 인접행렬형태
# 인접리스트방식은 인접행렬방식에 비해 정보를 얻는 속도가 느리다.
# O(N)의 시간복잡도, 스택자료구조

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
dfs(graph, 1, visited)