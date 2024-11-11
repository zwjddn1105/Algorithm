#import sys

#sys.stdin = open('sample_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    a, b = map(str, input().split())
    length_a = len(a)
    length_b = len(b)
    for i in range(length_a-length_b + 1):
        if a[i:i+length_b] == b:
            a = a.replace(b, 'x')

    count = 0
    for i in a:
        count += 1

    print(f'#{tc} {count}')