# 첫 원소는 이미 정렬되어 있다고 가정, 
# 적절한 위치에 삽입하는 과정을 n-1번 반복
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]: # 한 칸씩 왼쪽으로 이동
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break

print(arr)

# 시간복잡도는 O(N**2) 근데 거의 정렬되어있다면 매우 빠르게 동작함
# 최선의 경우엔 O(N)으로 끝
# 정렬이 거의 되어있다면 퀵정렬보다 빠름