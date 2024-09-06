#import sys

#sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n, b = map(int, input().split())
    h = list(map(int, input().split()))

    result = float('inf')
    def check(height, cnt):
        global result
        if height >= b:
            result = min(height, result)
            return
        if cnt == n:
            return

        check(height + h[cnt], cnt+1)
        check(height, cnt+1)

    check(0,0)

    print(f'#{tc} {abs(result-b)}')