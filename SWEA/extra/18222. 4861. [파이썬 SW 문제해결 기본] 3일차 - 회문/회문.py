# import sys

# sys.stdin = open('4861_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n, m = map(int, input().split())
    lst = [list(map(str, input().split())) for _ in range(n)]

    # 가로로 슬라이싱
    for i in range(n):
        for j in range(n-m+1):
            a = lst[i][0][j:j+m]
            reverse_a = a[::-1]
            if a == reverse_a:
                print(f'#{tc} {a}')
                break

    # 세로로 슬라이싱
    for i in range(n):
        result_2 = ''
        for j in range(n):
            result_2 += lst[j][0][i]
        reverse_result_2 = result_2[::-1]
        if result_2 == reverse_result_2:
            print(f'#{tc} {result_2}')