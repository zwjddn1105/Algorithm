# 특정조건이 부합할 때만 쓸 수 있다.
# 최악의 경우에도 O(N+K), 데이터 개수가 N, 최대값의 크기가 K
# 근데 데이터범위가 제한되고, 정수일때만 가능
# 모든 범위를 담을 수 있는 크기의 리스트를 선언해야 하기 때문
# 비교기반 정렬알고리즘이 아님, 다른건 다 비교기반

# 모든 원소의 값이 0보다 크거나 같다고 가정
arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count = [0] * (max(arr)+1)

for i in range(len(arr)):
    count[arr[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ') # 0 0 1 1 2 2 3 4 5 5 6 7 8 9 9 

# 기수정렬과 더불어 가장빠르다.
# 기수정렬: 1의자리기준정렬, 10자리기준, 100자리기준 ...