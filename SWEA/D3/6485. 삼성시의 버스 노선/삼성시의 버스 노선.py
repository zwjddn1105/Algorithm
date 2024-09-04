T = int(input())
for tc in range(1, T+1):
    n = int(input())
 
    cnt_lst = [0] * 5001
 
    for i in range(n):     
        start, end = map(int, input().split())
        for j in range(start, end+1):
            cnt_lst[j] += 1
     
    print(f'#{tc}', end=' ')
 
    p = int(input())
    for bus_stop in range(p):
        bus_stop = int(input())
        print(cnt_lst[bus_stop], end=' ')
    print()
