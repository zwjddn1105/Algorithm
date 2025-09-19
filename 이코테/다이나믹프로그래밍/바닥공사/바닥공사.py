import sys
n = int(sys.stdin.readline().rstrip())

dp = [0]*(n+1)
dp[1] = 1
dp[2] = 3

# 수학적으로 잘 생각해보면 이게 맞다는걸 깨달아야 함
for i in range(3, n+1):
    dp[i] = (dp[i-2]*2 + dp[i-1]) % 796796

print(dp[n])

