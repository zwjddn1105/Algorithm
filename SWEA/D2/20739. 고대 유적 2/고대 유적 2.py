T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_v = 0           # 가장 긴 구조물 길이
    for i in range(n):  # i행에서 가로 구조물 길이 확인
        cnt = 0             # 구조물 길이
        for j in range(m):
            if arr[i][j]:   # 구조물이면
                cnt += 1
                max_v = max(max_v, cnt)
            else:
                cnt = 0

    for i in range(m):  # j열에서 세로 구조물 길이 확인
        cnt = 0
        for j in range(n):
            if arr[j][i]:   # 구조물인 경우
                cnt += 1
                max_v = max(max_v, cnt)
            else:
                cnt = 0

    if max_v == 1:  # 노이즈인 경우
        max_v = 0
        
    print(f'#{tc} {max_v}')