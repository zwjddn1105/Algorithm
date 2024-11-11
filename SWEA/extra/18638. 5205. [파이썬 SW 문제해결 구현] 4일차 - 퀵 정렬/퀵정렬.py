#import sys

#sys.stdin = open('5205_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    def quick_sort(lst):
        if len(lst) <= 1:
            return lst
        pivot = lst[0]
        others = lst[1:]
        left_sides = [i for i in others if i <= pivot]
        right_sides = [i for i in others if i > pivot]
        return quick_sort(left_sides) + [pivot] + quick_sort(right_sides)

    sort_arr = quick_sort(arr)
    mid = (0 + (n-1)) // 2
    answer = sort_arr[mid+1]
    print(f'#{tc} {answer}')