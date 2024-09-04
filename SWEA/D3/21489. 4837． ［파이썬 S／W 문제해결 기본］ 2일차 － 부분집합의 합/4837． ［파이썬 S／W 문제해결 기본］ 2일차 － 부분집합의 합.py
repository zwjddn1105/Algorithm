# import sys
 
# sys.stdin = open('4837_input.txt')
 
# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    N, K = map(int, input().split())
 
    length_A = len(A)
    # 모든 부분집합을 저장할 리스트
    subset_list = []
    for i in range(1 << length_A):
        subset = []
        for j in range(length_A):
            if i & (1 << j):
                subset.append(A[j])
        subset_list.append(subset)
 
    cnt = 0
 
    for sub in subset_list:
        if len(sub) == N:
            s = 0
            for q in sub:
                s += q
            if s == K:
                cnt += 1
    print(f'#{tc} {cnt}')
