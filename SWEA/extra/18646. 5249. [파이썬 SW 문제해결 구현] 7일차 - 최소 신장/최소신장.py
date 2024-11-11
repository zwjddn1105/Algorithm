#import sys
import heapq
#sys.stdin = open('5249_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    visited = [0]*(v+1)
    def prim(start):
        q = []
        sum_weight = 0
        heapq.heappush(q, (0, start))

        while q:
            weight, node = heapq.heappop(q)
            if visited[node]:
                continue
            visited[node] = 1
            sum_weight += weight
            for next, value in graph[node]:
                if visited[next]:
                    continue
                heapq.heappush(q, (value, next))
        return sum_weight

    answer = prim(0)

    print(f'#{tc} {answer}')