# import sys

# sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    from collections import deque
    lst = list(map(int, input().split()))
    n = len(lst)

    subset_list = deque()    # 모든 부분집합을 저장할 리스트
    for i in range(1 << n):
        subset = deque()
        for j in range(n):
            if i & (1 << j):
                subset.append(lst[j])
        subset_list.append(subset)
    subset_list.popleft()

    for sub in subset_list :
        s = 0
        result = 0
        for q in sub:
            s += q
        if s == 0:
            result = 1
            break

    print(f'#{tc} {result}')