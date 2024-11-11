#import sys

#sys.stdin = open('5174_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    E, n = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(E+2)]
    for i in range(0, len(arr), 2):
        parent, child = arr[i], arr[i+1]
        graph[parent].append(child)

    for i in range(E+2):
        while len(graph[i]) < 2:
            graph[i].append(-1)
    cnt = 0
    def inorder_traversal(node):        # 어떤 순회로 해도 상관없음
        global cnt
        if node != -1:
            left, right = graph[node][0], graph[node][1]
            inorder_traversal(left)
            cnt += 1
            inorder_traversal(right)

    inorder_traversal(n)

    print(f'#{tc} {cnt}')
