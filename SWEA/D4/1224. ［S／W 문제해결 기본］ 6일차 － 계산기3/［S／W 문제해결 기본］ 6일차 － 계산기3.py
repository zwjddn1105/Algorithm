#import sys

#sys.stdin = open('input.txt')

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    length = int(input())
    data = input()
    stack = []
    result = []
    isp = {'(': 0, '+': 1, '*': 2, ')': -1}  # 안
    icp = {'(': 3, '+': 1, '*': 2, ')': -1}  # 밖
    # 후위 표기식 만들기
    for i in data:
        if i.isdigit():
            result.append(i)
        elif i == ')':
            while stack[-1] != '(':
                k = stack.pop()
                result.append(k)
            stack.pop()
        else:
            if stack:
                while stack:
                    if icp[i] <= isp[stack[-1]]:
                        p = stack.pop()
                        result.append(p)
                    else:
                        break
                stack.append(i)
            else:
                stack.append(i)

    while stack:
        c = stack.pop()
        result.append(c)

    answer = "".join(result)

    # 후위 표기식 계산
    stack2 = []
    for i in answer:
        if i == '+':
            c = stack2.pop()
            d = stack2.pop()
            value = (d+c)
            stack2.append(value)
        elif i == '*':
            c = stack2.pop()
            d = stack2.pop()
            value = (d*c)
            stack2.append(value)
        elif i.isdigit():
            stack2.append(int(i))
    number = stack2.pop()

    print(f'#{tc} {number}')