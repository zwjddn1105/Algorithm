# 이 코드는 시간적인 측면에서 비효율적

arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

        # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
        quick_sort(array, start, right-1)
        quick_sort(array, right+1, end)

quick_sort(arr, 0, len(arr)-1)
print(arr) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array 
    
    pivot = array[0]
    tail = array[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(arr)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 시간복잡도는 O(NlogN)
# 최악의경우 O(N**2) -> 이미 데이터가 정렬되어있는경우, 삽입정렬과 반대