#import sys

#sys.stdin = open('5201_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n, m = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    weight.sort(reverse=True)
    truck.sort(reverse=True)
    result = 0
    truck_idx = 0
    container_idx = 0
    while True:
        if truck_idx == m or container_idx == n:
            break
        if truck[truck_idx] >= weight[container_idx]:
            result += weight[container_idx]
            container_idx += 1
            truck_idx += 1
        else:
            container_idx += 1
    print(f'#{tc} {result}')