#import sys

#sys.stdin = open('4866_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    data = input()
    top = -1
    stack = []
    result = 1

    def ft_push(item):
        global top
        top += 1
        stack.append(item)

    def ft_pop():
        global top
        top -= 1
        stack.pop()

    for string in data:
        if string == '(' or string == '{':
            ft_push(string)
        if string == '}':
            if stack[top] == '{':
                ft_pop()
            else:
                result = 0
                break
        if string == ')':
            if stack[top] == '(':
                ft_pop()
            else:
                result = 0
                break
        if (string == ')' or string == '}') and stack == False:
            result = 0
            break
    else:
        if stack:
            result = 0
        

    print(f'#{tc} {result}')