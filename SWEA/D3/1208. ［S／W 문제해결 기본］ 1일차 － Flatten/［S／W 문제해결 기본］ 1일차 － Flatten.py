T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    dumps = int(input())
    arr = list(map(int, input().split()))

    result = 0
    for dump in range(dumps):
        max_v, max_idx = -1, 0
        min_v, min_idx = 101, 0
        # arr를 순회하며 최대, 최소 값과 인덱스 저장
        for idx, v in enumerate(arr):
            # 최댓값 저장
            if max_v < v:
                max_v = v
                max_idx = idx
            # 최솟값 저장
            if min_v > v:
                min_v = v
                min_idx = idx

        # 더 이상 수행할 수 없을 때
        if max_v - min_v <= 1:
            break
        # 덤프 수행하기
        else:
            arr[max_idx] -= 1
            arr[min_idx] += 1

    max_val = -1
    min_val = 101
    # 최종값 도출 (최대, 최소를 구하고 차이 구하기)
    for v in arr:
        # 최댓값 저장
        if max_val < v:
            max_val = v
        # 최솟값 저장
        if min_val > v:
            min_val = v

    result = max_val - min_val


    print(f'#{tc} {result}')