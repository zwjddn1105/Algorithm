T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result_a = 0
    result_b = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                result_a += arr[i][j]
   
    for i in range(n):
        for j in range(n):
            if i == n-1-j:
                result_b += arr[i][j]
    
    final_result = result_a + result_b
    # 가장 정중앙은 두번계산되므로 하나 빼줘야함
    k = n//2
    final_result -= arr[k][k]
    print(f'#{tc} {final_result}')