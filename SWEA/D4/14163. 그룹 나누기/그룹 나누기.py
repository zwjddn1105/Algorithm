#import sys
#sys.stdin = open('5248_input.txt')
def make_set(n):
    parent = [i for i in range(n)]
    rank = [0] * n
    return parent, rank

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
    parents, ranks = make_set(n)
    data = list(map(int, input().split()))

    for i in range(0, len(data), 2):
        union(data[i+1]-1, data[i]-1)

    for i in range(n):
        find(i-1)
    
    parents = set(parents)

    print(f'#{tc} {len(parents)}')