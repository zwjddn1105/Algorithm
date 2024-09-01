T = int(input())
for j in range(1, T + 1):
    n = int(input())
 
    factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n = n / i
        else:
            i = i + 1
 
    a=0
    b=0
    c=0
    d=0
    e=0
    for k in factors:
        if k == 2:
            a += 1
        elif k == 3:
            b += 1
        elif k == 5:
            c += 1
        elif k == 7:
            d += 1
        elif k == 11:
            e += 1
 
    print(f'#{j} {a} {b} {c} {d} {e}')