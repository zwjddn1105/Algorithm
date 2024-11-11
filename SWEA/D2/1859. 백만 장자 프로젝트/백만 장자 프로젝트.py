#import sys

#sys.stdin = open('input.txt')

from collections import deque
# Testcase 수
T = int(input())
# Testcase 만큼 반복

for tc in range(1, T+1):
    n = int(input())
    price = deque(map(int, input().split()))
    profit = 0

    def calculate(price):
        global profit
        max_price = price[0]
        for i in price:
            if max_price < i:
                max_price = i
                
        while True:
            k = price.popleft()
            if k != max_price:
                profit += abs(k - max_price)
            else:
                break
        return profit

    while price:
        calculate(price)

    print(f'#{tc} {profit}')
