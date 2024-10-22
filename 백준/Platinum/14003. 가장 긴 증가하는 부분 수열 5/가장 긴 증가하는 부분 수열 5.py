n = int(input())
lst = list(map(int, input().split()))


def binary_search(arr, num):
    start, end = 0, len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < num:
            start = mid + 1
        else:
            end = mid
    return start


def LIS(seq):
    if not seq:
        return []

    length_arr = []  # LIS 길이를 관리하는 배열
    index_arr = []   # 각 값의 인덱스를 기록
    prev = [-1] * len(seq)  # 이전 인덱스를 추적할 배열

    for i, num in enumerate(seq):
        idx = binary_search(length_arr, num)
        
        if idx == len(length_arr):
            length_arr.append(num)
            index_arr.append(i)
        else:
            length_arr[idx] = num
            index_arr[idx] = i

        if idx > 0:
            prev[i] = index_arr[idx - 1]  # 이전 값의 인덱스를 저장

    # 역추적하여 실제 LIS 구하기
    lis_length = len(length_arr)
    lis = []
    idx = index_arr[-1]  # LIS의 마지막 값의 인덱스

    for _ in range(lis_length):
        lis.append(seq[idx])
        idx = prev[idx]

    lis.reverse()  # 역순으로 만들었으므로 순서를 뒤집기

    return lis

result = LIS(lst)
print(len(result))
print(*result)