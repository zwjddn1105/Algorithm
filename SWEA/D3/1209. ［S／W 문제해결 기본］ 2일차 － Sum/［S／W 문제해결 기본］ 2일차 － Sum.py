#import sys
 
#sys.stdin = open('input.txt')
 
# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 가로 합
    hor_sum = []
    s = 0
    for i in range(100):
        for j in range(100):
            s += arr[i][j]
        hor_sum.append(s)
        s = 0
    # 세로 합
    ver_sum = []
    d = 0
    for i in range(100):
        for j in range(100):
            d += arr[j][i]
        ver_sum.append(d)
        d = 0
    # 대각선 합
    cross_sum = []
    f = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                f += arr[i][i]
    cross_sum.append(f)
    f = 0
    for i in range(100):
        for j in range(100):
            if i == 99-j:
                f += arr[i][99-j]
    cross_sum.append(f)
 
    result_list = hor_sum + ver_sum + cross_sum
    max_result = result_list[0]
    for i in result_list:
        if max_result < i:
            max_result = i
 
    print(f'#{tc} {max_result}')