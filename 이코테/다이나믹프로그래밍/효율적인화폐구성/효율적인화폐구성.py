import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
money = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

dp = [1e9]*10001
dp[0] = 0
for i in range(1, m+1):
    for cash in money:
        if i-cash >= 0:
            dp[i] = min(dp[i], dp[i-cash] + 1)

if dp[m] == 1e9:
    print(-1)
else:
    print(dp[m])