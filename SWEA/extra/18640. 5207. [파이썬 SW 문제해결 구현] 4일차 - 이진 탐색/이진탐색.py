# import sys
#
# sys.stdin = open('5207_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    cnt = 0

    def binary_search(arr, target):
        lst = []
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                return lst
            elif arr[mid] < target:
                start = mid + 1
                lst.append(1)
            else:
                end = mid - 1
                lst.append(-1)
        return lst

    for i in B:
        if i not in A:
            continue
        lst = binary_search(A, i)
        if lst:
            for i in range(len(lst) - 1):
                if lst[i] == lst[i + 1]:
                    break
            else:
                cnt += 1
        else:
            cnt += 1

    print(f'#{tc} {cnt}')