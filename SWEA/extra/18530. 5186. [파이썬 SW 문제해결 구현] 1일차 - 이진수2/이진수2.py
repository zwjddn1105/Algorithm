#import sys

#sys.stdin = open('5186_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = float(input())
    binary = ''

    while n - int(n) > 0:
        n *= 2
        binary += str(int(n))
        n -= int(n)

    if len(binary) <= 12:
        print(f'#{tc} {binary}')
    else:
        print(f'#{tc} overflow')