#import sys

#sys.stdin = open('4874_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    data = list(map(str, input().split()))
    stack = []
    for i in data:
        if i.isdigit():
            stack.append(int(i))
        elif i == '*' and len(stack) > 1:
            c = stack.pop()
            d = stack.pop()
            value = d*c
            stack.append(value)
        elif i == '+' and len(stack) > 1:
            c = stack.pop()
            d = stack.pop()
            value = d+c
            stack.append(value)
        elif i == '-' and len(stack) > 1:
            c = stack.pop()
            d = stack.pop()
            value = d-c
            stack.append(value)
        elif i == '/' and len(stack) > 1:
            c = stack.pop()
            d = stack.pop()
            value = d/c
            stack.append(value)
        elif i == '.':
            if len(stack) == 1:
                result = int(stack.pop())
                print(f'#{tc} {result}')
            else:
                print(f'#{tc} error')
        else:
            print(f'#{tc} error')
            break