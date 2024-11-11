#import sys

#sys.stdin = open('input.txt')

# Testcase 수
T = 1
# Testcase 만큼 반복
for tc in range(1, T+1):
    v = int(input())
    arr = list(map(int, input().split()))

    # 자식 노드들
    left = [0] * (v+1)
    right = [0] * (v+1)

    for i in range(0, len(arr), 2):
        parent = arr[i]
        child = arr[i+1]
        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child

    def preorder(node):
        if node == 0:
            return
        print(node, end=' ')
        preorder(left[node])
        preorder(right[node])

    preorder(1)
