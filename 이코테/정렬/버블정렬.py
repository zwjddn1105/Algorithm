def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:   # 더 이상 교환이 없으면 이미 정렬됨
            break


arr = [64, 34, 25, 12, 57, 93, 1, 123]

bubbleSort(arr)

print(arr) # [1, 12, 25, 34, 57, 64, 93, 123]
