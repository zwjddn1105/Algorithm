#import sys

#sys.stdin = open('input.txt')

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    n, m = map(str, input().split())

    stack = []
    top = -1

    for i in m:
        if len(stack) == 0:
            top += 1
            stack.append(i)
        elif stack:
            if stack[top] == i:
                top -= 1
                stack.pop()
            else:
                top += 1
                stack.append(i)

    result = ''
    for k in stack:
        result += k

    print(f'#{tc} ', end='')
    print(result)