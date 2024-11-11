#import sys

#sys.stdin = open('5176_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    # 중위순회
    # 그래프 만들기
    graph = [[] for _ in range(n+1)]
    for i in range(2, n+1):
        i_parent_idx = i // 2
        graph[i_parent_idx].append(i)
    # 인덱스 오류 방지 -1값 추가
    for i in range(n+1):
        while len(graph[i]) < 2:
            graph[i].append(-1)

    inorder_tra = []

    def inorder_traversal(node):
        if node != -1:
            left, right = graph[node][0], graph[node][1]
            inorder_traversal(left)
            inorder_tra.append(node)
            inorder_traversal(right)

    inorder_traversal(1)

    root = 1
    find = n // 2
    a = inorder_tra.index(find) + 1
    b = inorder_tra.index(root) + 1


    print(f'#{tc} {b} {a}')