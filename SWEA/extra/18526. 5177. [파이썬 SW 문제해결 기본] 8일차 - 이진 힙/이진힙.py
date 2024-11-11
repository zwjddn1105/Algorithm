#import sys

#sys.stdin = open('5177_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    def enq(n):
        global last
        last += 1
        h[last] = n
        c = last
        p = c // 2  # 부모번호 계산
        while p >= 1 and h[p] > h[c]:
            h[p], h[c] = h[c], h[p]
            c = p
            p = c // 2

    h = [0]*(n+1)
    last = 0
    for i in arr:
        enq(i)
    last_node = len(arr)
    result = 0
    result -= h[last_node]
    while last_node >= 1:
        result += h[last_node]
        last_node //= 2

    print(f'#{tc} {result}')
