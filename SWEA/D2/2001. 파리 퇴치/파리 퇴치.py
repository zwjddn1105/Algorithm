T =int(input())
for tc in range(1, T+1):
    n,m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    fly = []
    for i in range(n-m+1):
        for j in range(n-m+1):
            cnt = 0
            for x in range(m):
                for y in range(m):
                    cnt += arr[i+x][j+y]
                    fly.append(cnt)
    max_fly = fly[0]
    for i in fly:
        if max_fly < i:
            max_fly = i
    print(f'#{tc} {max_fly}')
