# 다익스트라 최단경로 알고리즘은 기본적으로 그리디 알고리즘으로 분류된다.
# 다익스트라 알고리즘의 시간복잡도는 O(V^2), V는 노드의 개수

# 간단한 다익스트라 알고리즘 소스코드, 이건 노드개수가 1만개 이하일 때만 써먹을만 함
import sys 
INF = 1e9

n, m = map(int, sys.stdin.readline().rstrip().split()) # 노드, 간선의 개수
start = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1) # 방문했는지 체크
distance = [INF] * (n+1) # 최단거리 테이블

for _ in range(m): # 모든 간선 정보 입력받기
    a, b, c = map(int, sys.stdin.readline().rstrip().split()) # a번에서 b번노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

def get_smallest_node(): # 방문하지 않은 노드 중, 가장 최단 거리가 짧은 노드의 번호를 반환
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드의 인덱스
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n-1): # 시작노드제외 전체 n-1개 노드에 대해 반복
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]: # 현재 노드와 연결 된 다른 노드를 확인
            cost = distance[now] + j[1]
            if cost < distance[j[0]]: # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[j[0]] = cost
dijkstra(start)

# 모든 노드로 가는 최단거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])