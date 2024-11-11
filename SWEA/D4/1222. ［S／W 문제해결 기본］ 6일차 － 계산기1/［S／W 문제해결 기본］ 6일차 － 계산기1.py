#import sys

#sys.stdin = open('input.txt')

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    length = int(input())
    n = input()
    result = []
    stack = []
    # 후위 표기식 만들기
    for i in range(length):
        if n[i] == '+':
            if stack:
                a = stack.pop()
                result.append(a)
                stack.append(n[i])
            else:
                stack.append(n[i])
        elif type(int(n[i])) == int:
            result.append(n[i])
    else:
        if stack:
            b = stack.pop()
            result.append(b)

    # 후위 표기식 계산하기
    stack2 = []
    for i in result:
        if i == '+':
            c = stack2.pop()
            d = stack2.pop()
            value = (d+c)
            stack2.append(value)
        elif type(int(i)) == int:
            stack2.append(int(i))
    answer = stack2.pop()
    print(f'#{tc} {answer}')