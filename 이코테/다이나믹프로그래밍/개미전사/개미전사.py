import sys
n = int(sys.stdin.readline().rstrip())
food = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [0]*(n+1)
dp[1] = food[0]
dp[2] = max(food[0], food[1])
for i in range(3, n+1):
    dp[i] = max(dp[i-2] + food[i-1], dp[i-1])

print(dp[n])
