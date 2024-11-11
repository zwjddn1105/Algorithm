T = 1
for tc in range(1,T+1):
    def f(i, k, s, t):     # 원소, 집합의크기, i-1까지합, 목표
        global cnt
        if s > t:        
            return
        elif s == t:
            cnt +=1
        elif i == k:
            return
        else:
            bit[i] = 1
            f(i+1, k, s+data[i], t)
            bit[i] = 0
            f(i+1, k, s, t)

    data = list(map(int, input().split()))
    n =len(data)
    cnt = 0 # 합이 key와같은 부분집합의 수
    bit = [0]*n

    f(0, n, 0, 10)
    print(f'#{tc} {cnt}')