# import sys

# sys.stdin = open('4869_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    num = n // 10

    def origami(n):
        if n == 1:
            return 1
        if n == 2:
            return 3
        return 2*origami(n-2) + origami(n-1)

    result = origami(num)

    print(f'#{tc} {result}')