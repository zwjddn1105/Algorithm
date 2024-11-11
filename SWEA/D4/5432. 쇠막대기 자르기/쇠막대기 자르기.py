# import sys

# sys.stdin = open('sample_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    data = input()
    counts = 0
    for i in range(len(data)):
        if data[i:i+2] == '()':
            counts += 1
    new_data = data.replace('()', 'x', counts)

    stick = 0
    result = 0

    for i in range(len(new_data)):
        if new_data[i] == '(':
            stick += 1
        elif new_data[i] == ')':
            stick -= 1
            result += 1
        elif new_data[i] == 'x':
            result += stick

    print(f'#{tc} {result}')
