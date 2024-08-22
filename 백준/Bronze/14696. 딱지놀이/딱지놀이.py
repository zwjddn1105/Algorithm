n = int(input())
for _ in range(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.pop(0)
    b.pop(0)
    a.sort(reverse=True)
    b.sort(reverse=True)
    stop = False
    while a and b:
        c = a.pop(0)
        d = b.pop(0)
        if c>d:
            print('A')
            stop = True
            break
        elif c<d:
            print('B')
            stop = True
            break
    if stop:
        continue
    else:
        if len(a)>len(b):
            print('A')
        elif len(a)<len(b):
            print('B')
        elif len(a)==len(b):
            print('D')