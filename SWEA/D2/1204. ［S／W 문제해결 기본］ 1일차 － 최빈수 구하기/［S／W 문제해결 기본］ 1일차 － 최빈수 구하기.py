T = int(input())
for tc in range(1,1+T):
    n = int(input())
    arr = list(map(int, input().split()))
 
    cnt_lst = [0 for _ in range(101)] # 0점부터 100점
 
    for i in arr:
        cnt_lst[i] += 1
 
    mode = cnt_lst[0]
    for i in range(len(cnt_lst)):
        if mode <= cnt_lst[i]: 
            mode = cnt_lst[i]
            result = i
 
    print(f'#{n} {result}')
