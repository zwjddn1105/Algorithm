def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  # 정렬된 결과 저장용
    count = [0] * 10  # 자릿수(0~9) 카운트

    # 해당 자리수 기준으로 count 배열 채우기
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # 누적합으로 변환
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 결과 배열 만들기 (안정정렬)
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # 원래 배열에 정렬된 결과 복사
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # 최대값을 기준으로 자릿수 구하기
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        print(arr)
        '''
        [170, 90, 802, 2, 24, 45, 75, 66]
        [802, 2, 24, 45, 66, 170, 75, 90]
        [2, 24, 45, 66, 75, 90, 170, 802]
        '''
        exp *= 10

# 사용 예시
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("정렬 결과:", arr) # [2, 24, 45, 66, 75, 90, 170, 802]
