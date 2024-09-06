#import sys

#sys.stdin = open('sample_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    price = list(map(int, input().split()))
    plan = [0] + list(map(int, input().split()))

    dp = [0]*13
    for i in range(1, 13):
        if i > 2:
            dp[i] = min(dp[i-1] + plan[i]*price[0], dp[i-1]+price[1], dp[i-3] + price[2])
        elif i <= 2:
            dp[i] = min(dp[i-1] + plan[i]*price[0], dp[i-1]+price[1])

    result = dp[12]
    result = min((price[3]), result)

    print(f'#{tc} {result}')