#import sys

#sys.stdin = open('5204_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    start = 0
    end = n - 1
    middle = (start + end) // 2
    cnt = 0
    def merge_sort(arr):
        if len(arr) < 2:
            return arr
        mid = len(arr) // 2
        left_arr = merge_sort(arr[:mid])
        right_arr = merge_sort(arr[mid:])
        return merge(left_arr, right_arr)

    def merge(left, right):
        global cnt
        i = j = 0
        merge_array = []
        if left[-1] > right[-1]:
            cnt += 1
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merge_array.append(left[i])
                i += 1
            else:
                merge_array.append(right[j])
                j += 1
        merge_array += left[i:]
        merge_array += right[j:]
        return merge_array

    sort_array = merge_sort(arr)
    middle_value = sort_array[middle+1]

    print(f'#{tc} {middle_value} {cnt}')
