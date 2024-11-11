#import sys

#sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    string = ''
    arr = [input().split() for _ in range(n)]
    for i in range(n):
        string += arr[i][0]

    def solve(binary):
        value = 0
        binary = binary[::-1]
        for i in range(7):
            value += int(binary[i])*(2**(i))
        return value
    print(f'#{tc}', end=' ')
    for i in range(0, len(string)-1, 7):
        binary = string[i:i+7]
        print(solve(binary), end=' ')