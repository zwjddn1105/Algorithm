# 가장 작은 데이터를 앞으로 보내는 과정을 n-1번 반복
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
length = len(arr)

for i in range(length):
    min_idx = i # 가장 작은 원소의 인덱스
    for j in range(i+1, length):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]