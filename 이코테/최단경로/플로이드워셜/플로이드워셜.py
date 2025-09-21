# 다익스트라는 한 지점에서 다른 특정 지점까지의 최단경로
# 플로이드 워셜은 모든 지점에서 다른 모든지점까지의 최단경로
# N번의 단계, 단계마다 O(N^2)의 연산을 통해 현재 노드를 거쳐가는 모든 경로를 고려한다.
# 그래서 총 시간복잡도는 O(N^3)
# 다익스트라는 그리디이지만, 플로이드워셜은 dp이다.
# 플로이드워셜의 점화식은 Dab = min(Dab, Dak + Dkb)
INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1): # 자기 자신으로 가는 비용은 0으로 초기화
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m): # 간선정보 입력
    a,b,c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1): # 점화식대로 플로이드워셜 알고리즘 수행
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print('INFINITY', end=' ')
        else:
            print(graph[a][b], end=' ')
    print()

'''
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2


0 4 8 6
3 0 7 9
5 9 0 4
7 11 2 0
'''