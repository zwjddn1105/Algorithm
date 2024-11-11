#import sys
from collections import deque
#sys.stdin = open('input.txt')

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    length, start = map(int, input().split())
    data = list(map(int, input().split()))
    max_num = max(data)
    graph = [set() for _ in range(max_num+1)]
    visited = [0] * (max_num + 1)

    for i in range(0, length, 2):
        graph[data[i]].add(data[i+1])

    q = deque()
    q.append((start, 0))
    visited[start] = True
    answer = 0
    order = 0

    def bfs():
        global answer, order
        while q:
            num, cnt = q.popleft()
            if cnt > order:
                order = cnt
                answer = num
            elif cnt == order:
                if answer < num:
                    answer = num
            for i in graph[num]:
                if not visited[i]:
                    q.append((i, cnt+1))
                    visited[i] = True
    bfs()

    print(f'#{tc} {answer}')