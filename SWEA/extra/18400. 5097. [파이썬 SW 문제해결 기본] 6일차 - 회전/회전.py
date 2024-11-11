#import sys

#sys.stdin = open('5097_input.txt')
from collections import deque

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = deque(map(int, input().split()))
        
    def move_number(nums):
        a = nums.popleft()
        nums.append(a)
        return nums

    for _ in range(M):
        move_number(nums)

    result = nums[0]

    print(f'#{tc} {result}')

