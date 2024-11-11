# import sys

# sys.stdin = open('ex1_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    sum_list = []

    for i in range(N):
        for j in range(N):
            s = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    s += abs(arr[nx][ny] - arr[i][j])
            sum_list.append(s)

    result_sum = 0
    for q in sum_list:
        result_sum += q
    print(f'#{tc} {result_sum}')