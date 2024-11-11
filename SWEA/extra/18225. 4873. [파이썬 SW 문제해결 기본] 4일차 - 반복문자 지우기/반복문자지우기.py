#import sys

#sys.stdin = open('4873_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    data = list(input())
    stack = []
    top = -1

    for i in data:
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

    result = len(stack)
    print(f'#{tc} {result}')



