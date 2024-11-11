#import sys

#sys.stdin = open('input.txt')


# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    graph = [[0, 0, 0] for i in range(n+1)]
    for i in range(n):
        arr = input().split()
        if len(arr) == 4:
            v = int(arr[0])
            graph[v][0] = arr[1]
            graph[v][1] = int(arr[2])
            graph[v][2] = int(arr[3])
        elif len(arr) == 2:
            v = int(arr[0])
            graph[v][0] = int(arr[1])

    for i in range(n+1):
        for j in range(3):
            if graph[i][j] == 0:
                graph[i][j] = -1

    result = []

    def postorder_traversal(node):
        global result
        string, left, right = graph[node][0], graph[node][1], graph[node][2]
        if node != -1:
            postorder_traversal(left)
            postorder_traversal(right)
            if string == '+':
                b = result.pop()
                a = result.pop()
                c = a+b
                result.append(c)
            elif string == '-':
                b = result.pop()
                a = result.pop()
                c = a-b
                result.append(c)
            elif string == '*':
                b = result.pop()
                a = result.pop()
                c = a*b
                result.append(c)
            elif string == '/':
                b = result.pop()
                a = result.pop()
                c = a/b
                result.append(c)
            else:
                result.append(string)
    postorder_traversal(1)
    print(f'#{tc} {int(result[0])}')
