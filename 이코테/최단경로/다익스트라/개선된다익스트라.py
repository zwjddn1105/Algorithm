# 이 구현 방법을 이용하면 최악의 경우에도 시간 복잡도 O(ElogV)를 보장하여 해결. E는 간선의개수, V는 노드의개수
# 간단한 다익스트라 알고리즘 과정에서 최단 거리가 가장 짧은 노드를 찾는 get_뭐시기 이거 할때 O(V)의 시간
# 선형적으로 탐색했기 때문, 그러나 최단 거리 노드를 선형적으로 찾는 것이 아니라 더 빠르게 찾는 방법이 있다.
# 이를 적용한 것이 개선된 다익스트라 알고리즘
# 힙 자료구조를 사용해야 함 -> 선형 시간이 아닌 로그 시간이 걸린다.
# 정확히는 우선순위 큐를 구현하기 위하여 힙자료구조를 사용하는 것
# 큐를 구현하기 위해서 덱을 사용하는것과 같음
# 파이썬에선 우선순위 큐는 PriorityQueue랑 heapq를 사용할 수 있는데 heapq가 더 빠르기 때문에 이것 사용을 권장함.
# 리스트로 우선순위 큐를 구현할 수도 있는데 이거는 데이터 1개당 삽입은 O(1)이지만 삭제가 최악의 경우에 O(N)의 시간복잡도
# 힙은 삽입, 삭제 모두 O(NlogN)의 시간복잡도

import heapq
import sys
INF = int(1e9)
n, m = map(int, sys.stdin.readline().rstrip().split())
start = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b,c)) # 거리, 노드

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 현재 노드가 이미 처리된 적 있는 노드이면 무시, 전체 노드의 개수 V보다 더 많은 노드가 들어갈 일이 없다.
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)
for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])

'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3 
4 5 1
5 3 1
5 6 2

0
2
3
1
2
4
'''