#import sys

#sys.stdin = open('sample_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    data = input()
    stack = []
    result = []
    isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, ')': -1} # 안
    icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2, ')': -1} # 밖
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
                while icp[i] <= isp[stack[-1]]:
                    p = stack.pop()
                    result.append(p)
                else:
                    stack.append(i)
            else:
                stack.append(i)

    while stack:
        c = stack.pop()
        result.append(c)

    answer = "".join(result)
    print(f'#{tc} {answer}')

