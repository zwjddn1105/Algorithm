#import sys

#sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    v, e, s1, s2 = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(v+1)]
    parent_lst = [0] * (v+1)
    common = 0
    for i in range(0, len(arr), 2):
        parent, child = arr[i], arr[i+1]
        parent_lst[child] = parent
        graph[parent].append(child)

    for i in range(v+1):
        while len(graph[i]) < 2:
            graph[i].append(-1)

    s1_parent = []
    while parent_lst[s1] != 0:
        s1_parent.append(parent_lst[s1])
        s1 = parent_lst[s1]

    while True:
        if parent_lst[s2] in s1_parent:
            common = parent_lst[s2]
            break
        s2 = parent_lst[s2]

    cnt = 0
    def inorder_traversal(node):
        global cnt
        left, right = graph[node][0], graph[node][1]
        if node != -1:
            inorder_traversal(left)
            cnt += 1
            inorder_traversal(right)

    inorder_traversal(common)

    print(f'#{tc} {common} {cnt}')