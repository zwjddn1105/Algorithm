#import sys

#sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    data = []
    for i in range(n):
        if '1' in arr[i]:
            data = arr[i]
            break

    password = ''
    for i in range(m-1, -1, -1):
        if data[i] == '1':
            for j in range(i-55, i+1):
                password += data[j]
            break

    answer = []
    info = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3,
            '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
            '0110111': 8, '0001011': 9}

    for i in range(0, 56, 7):
        num = password[i:i+7]
        answer.append(info[num])

    for i in range(0, 8, 2):
        answer[i] = answer[i]*3

    if sum(answer) % 10 == 0:
        for i in range(0, 8, 2):
            answer[i] = answer[i] / 3
        print(f'#{tc} {int(sum(answer))}')
    else:
        print(f'#{tc} 0')