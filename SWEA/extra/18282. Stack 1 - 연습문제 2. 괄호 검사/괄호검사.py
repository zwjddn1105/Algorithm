#import sys

#sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    data = list(input().strip())
    top = -1
    stack = []
    result = 1

    def push(item):
        global top
        top += 1
        stack.append(item)

    def pop():
        global top
        top -= 1
        stack.pop()

    for i in data:
        if i == '(':
            push(i)
        elif i == ')' and stack:
            pop()
        elif i == ')' and (stack != True):
            result = -1
            break
    else:
        if stack:
            result = -1

    print(f'#{tc} {result}')