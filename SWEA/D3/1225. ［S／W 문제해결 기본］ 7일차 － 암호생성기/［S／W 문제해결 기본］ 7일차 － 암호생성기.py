#import sys

#sys.stdin = open('input.txt')

from collections import deque

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    arr = deque(map(int, input().split()))

    def cycle(arr):
        cnt = 1
        while True:
            k = cnt % 5
            if k == 0:
                k = 5
            number = arr.popleft() - k
            if number <= 0:
                number = 0
            arr.append(number)
            if number == 0:
                break
            cnt += 1
        return arr

    cycle(arr)

    print(f'#{tc}', end=' ')
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print()