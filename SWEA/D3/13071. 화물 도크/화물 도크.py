#import sys

#sys.stdin = open('5202_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key= lambda x: (-x[1], -x[0]))

    start, end = arr.pop()

    cnt = 1
    while arr:
        s, e = arr.pop()
        if end <= s:
            cnt += 1
            start, end = s, e

    print(f'#{tc} {cnt}')
