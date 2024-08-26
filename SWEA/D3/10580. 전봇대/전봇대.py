T = int(input())
for tc in range(1, T+1):
    n = int(input())
    wire = [list(map(int, input().split())) for _ in range(n)]
    wire.sort()     # x좌표는 낮은순부터 정렬

    cnt = 0         # 만나는 점의 개수

    # 첫 번째 줄은 교차점이 없으므로 1부터 시작
    for i in range(1, n):
        for j in range(i):  # j 줄을 그 전까지 그어진 줄과 교차점 구함
            if wire[j][1] > wire[i][1]: # a가 더 아래있지만 b가 더 높으면 교차점
                cnt += 1

    print(f'#{tc} {cnt}')