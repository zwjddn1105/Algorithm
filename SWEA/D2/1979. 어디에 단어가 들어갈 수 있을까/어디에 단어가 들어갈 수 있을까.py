T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0
 
 
    for i in range(n):
        hor = 0
        ver = 0
        for j in range(n):      
            if arr[i][j] == 1:
                hor += 1
            else:             
                if hor == k:
                    result += 1
                hor = 0
            if arr[j][i] == 1:
                ver += 1
            else:
                if ver == k:
                    result += 1
                ver = 0
        if hor == k:   
            result += 1
        if ver == k:
            result += 1
 
                 
 
    print(f'#{tc} {result}')