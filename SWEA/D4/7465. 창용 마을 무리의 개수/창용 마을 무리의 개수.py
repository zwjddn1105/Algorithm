#import sys
#sys.stdin = open('s_input.txt')
 
def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]
 
def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return
    if ranks[root_x] > ranks[root_y]:
        parents[root_y] = root_x
    elif ranks[root_x] < ranks[root_y]:
        parents[root_x] = root_y
    else:
        parents[root_y] = root_x
        ranks[root_x] += 1
# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n, m = map(int, input().split())
    parents = [i for i in range(n)]
    ranks = [0]*n
    for _ in range(m):
        a, b = map(int, input().split())
        # if a < b:
        #     union(a-1, b-1)
        # elif a > b:
        #     union(b-1, a-1)
        union(a-1, b-1)
 
    for i in range(n):
        find(i-1)
    parents = set(parents)
    print(f'#{tc} {len(parents)}')