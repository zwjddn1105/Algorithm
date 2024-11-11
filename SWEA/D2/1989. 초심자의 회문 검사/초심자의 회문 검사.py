# import sys

# sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = input()
    m = n[::-1]
    result = 0
    if n == m:
        result = 1
    print(f'#{tc} {result}')