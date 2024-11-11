#import sys

#sys.stdin = open('5099_input.txt')

from collections import deque

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ci = deque(map(int, input().split()))
    queue = deque()

    # 치즈와 문자인덱스 포함된 data 만들기
    for i in range(1, N+1):
        queue.append([ci.popleft(), i])

    while True:
        pizza = queue.popleft()
        pizza[0] //= 2
        if pizza[0] == 0:
            if len(ci) > 0:
                queue.append([ci.popleft(), N+1])
                N += 1
        else:
            queue.append(pizza)

        if len(queue) == 1:
            break
    result = queue[0][1]
    print(f'#{tc} {result}')