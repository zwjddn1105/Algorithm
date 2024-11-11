#import sys

#sys.stdin = open('5178_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n, m, l = map(int, input().split())
    graph = [[0, 0, 0] for _ in range(n+1)]
    for i in range(1, n+1):
        graph[i][1] = i*2
        graph[i][2] = i*2 + 1
    for i in range(m):
        arr = list(map(int, input().split()))
        graph[arr[0]][0] = arr[1]

    c = n
    while c >= 1:
        p = c//2
        graph[p][0] += graph[c][0]
        c -= 1
    result = graph[l][0]
    print(f'#{tc} {result}')
