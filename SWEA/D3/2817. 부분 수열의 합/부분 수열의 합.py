#import sys

#sys.stdin = open('sample_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))

    cnt = 0

    def check(now, total):
        global cnt
        if now == n:
            return
        if total + numbers[now] == k:
            cnt += 1

        check(now + 1, total)
        check(now + 1, total + numbers[now])

    check(0, 0)
    print(f'#{tc} {cnt}')
