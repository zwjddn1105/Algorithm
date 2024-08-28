#import sys
#sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]

    def check(tmp, idx, total):
        global min_total
        if idx == n:
            min_total = min(min_total, total)
            return
        if tmp == 'W' and idx < n-2:
            total += m - arr[idx].count('W')
            idx += 1
            check('W', idx, total)
            check('B', idx, total)
        elif tmp == 'B' and idx < n-1:
            total += m - arr[idx].count('B')
            idx += 1
            check('B', idx, total)
            check('R', idx, total)
        elif tmp == 'R' and idx < n:
            total += m - arr[idx].count('R')
            idx += 1
            check('R', idx, total)
    min_total = float('inf')
    check('W', 0, 0)
    print(f'#{tc} {min_total}')