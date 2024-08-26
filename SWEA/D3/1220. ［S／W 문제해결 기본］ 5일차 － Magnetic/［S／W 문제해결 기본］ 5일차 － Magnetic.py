# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    square_side = int(input())      # 어차피 100
    arr = [list(map(int, input().split())) for _ in range(square_side)]
    new_arr = [[0]*100 for _ in range(100)]
    cnt = 0     # 교착상태 수
    for i in range(100):        # 열 우선
        for j in range(100):
            new_arr[i][j] = arr[j][i]

    for i in range(100):
        result = ''
        for j in range(100):
            if new_arr[i][j]:
                result += str(new_arr[i][j])
        for k in range(len(result)-1):
            if result[k:k+2] == '12':
                cnt += 1

    print(f'#{tc} {cnt}')