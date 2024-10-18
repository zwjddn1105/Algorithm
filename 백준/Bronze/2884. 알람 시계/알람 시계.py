h, m = map(int, input().split())

if m-45 < 0:
    if h-1 == -1:
        print(23, end=' ')
        print(m-45+60)
    else:
        print(h-1, end=' ')
        print(m-45+60)
else:
    print(h, end=' ')
    print(m-45)