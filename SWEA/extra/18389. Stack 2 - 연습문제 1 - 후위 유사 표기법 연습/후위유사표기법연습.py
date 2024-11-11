#import sys

#sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    data = input()
    stack = []
    result = ''
    for i in data:
        if i in ['+', '-', '*', '/']:
            stack.append(i)
        elif i.isdigit():
            result += i
    while stack:
        b = stack.pop()
        result += b

    print(f'#{tc} {result}')