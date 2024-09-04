# import sys

# sys.stdin = open('4836_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    data.sort(key=lambda x: x[4])
    empty_arr = [[0] * 10 for _ in range(10)]
    for i in range(N):
        if data[i][-1] == 1:
            a = data[i][0]
            b = data[i][1]
            c = data[i][2]
            d = data[i][3]
            for j in range(a, c + 1):
                for k in range(b, d + 1):
                    if empty_arr[j][k] == 0:
                        empty_arr[j][k] = 1
        elif data[i][-1] == 2:
            e = data[i][0]
            f = data[i][1]
            g = data[i][2]
            h = data[i][3]
            for j in range(e, g + 1):
                for k in range(f, h + 1):
                    if empty_arr[j][k] == 1:
                        empty_arr[j][k] = 2

    count = 0
    for i in range(10):
        for j in range(10):
            if empty_arr[i][j] == 2:
                count += 1

    print(f'#{tc} {count}')