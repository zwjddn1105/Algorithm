#import sys

#sys.stdin = open('sample_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    a, b, c = map(int, input().split())
    cnt = 0

    while b >= c:
        b -= 1
        cnt += 1

    while a >= b:
        a -= 1
        cnt += 1

    if a == 0 or b == 0:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {cnt}')