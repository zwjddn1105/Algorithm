T = int(input())
for tc in range(1, T+1):
    k,n,m = map(int, input().split())
    bus_charge = map(int, input().split())
    
    arr = [False] * (n+1)
    for i in bus_charge:
        arr[i] = True
 
    # 충전횟수
    charge_cnt = 0
    # 현재위치
    now_point = 0

    while now_point < n:
        now_point += k
        find_charge = True  
        if now_point >= n:      
            break
        if arr[now_point]:      # 충전기가 있다면
            charge_cnt += 1   
        else:                   # 충전기가 없다면
            for i in range(1,k):
                if arr[now_point-i]:
                    charge_cnt += 1
                    now_point -= i
                    find_charge = True
                    break      
                else:
                    find_charge = False
        if find_charge == False:
            charge_cnt = 0
            break       # while문 break
                

    print(f'#{tc} {charge_cnt}')