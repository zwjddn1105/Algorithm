T = int(input())
 
for tc in range(1, 1+T):
    n,m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    lst = []
    for i in range(n):
        for j in range(m):
            pollen = arr[i][j]
            sum_pollen = arr[i][j]
            while pollen > 0: 
                for k in range(4):
                    ni = i + dx[k]*pollen
                    nj = j + dy[k]*pollen
                    if 0<=ni<n and 0<=nj<m:
                        sum_pollen += arr[ni][nj] 
                pollen -= 1
                lst.append(sum_pollen)
    # lst 내에서 최대값만 출력하면 끝
    result = lst[0]
    for i in range(1, len(lst)):
        if result < lst[i]:
            result = lst[i]
 
    print(f'#{tc} {result}')