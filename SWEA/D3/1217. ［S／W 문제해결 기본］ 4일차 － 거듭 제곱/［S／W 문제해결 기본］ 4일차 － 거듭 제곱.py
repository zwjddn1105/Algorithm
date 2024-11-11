#import sys

#sys.stdin = open('input.txt')

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    q_number = int(input())
    n, m = map(int, input().split())

    def f_nm(n, m):
        if m == 1:
            return n
        else:
            return n * f_nm(n, m-1)

    result = f_nm(n, m)
    print(f'#{tc} {result}')