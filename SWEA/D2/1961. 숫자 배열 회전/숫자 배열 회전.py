T = int(input())
for tc in range(1,1+T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
     
    list_arr90 = []
    list_arr180 = []
    list_arr270 = []
 
    for i in range(n):
        arr90 = []
        arr180 = []
        arr270 = []
        for j in range(n):
            arr90.append(arr[-j-1][i])
            arr180.append(arr[-i-1][-j-1])
            arr270.append(arr[j][-i-1])
        list_arr90.append(arr90)
        list_arr180.append(arr180)
        list_arr270.append(arr270) # 묶어주려고
    a = zip(list_arr90, list_arr180, list_arr270)
 
    print(f'#{tc}')
    for i in a:
        for j in i:
            for k in j:
                print(k, end='')
            print(' ', end='')
        print()