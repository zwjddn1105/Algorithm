T = int(input())
from collections import deque
for tc in range(1,T+1):
    n = int(input())
    numbers = deque(map(int, input().split()))
    count = 0
 
    def bubble_sort(arr):
        for i in range(len(arr)-1):
            for j in range(len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
 
    bubble_sort(numbers)
    print(f'#{tc}', end=' ')
    while count < 10:
        count += 1
        a = numbers.pop()
        print(a, end=' ')
        if count == 10:
            break
        count += 1
        b = numbers.popleft()
        print(b, end=' ')
    print()