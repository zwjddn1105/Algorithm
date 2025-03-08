while True:
    lst = list(map(int, input().split()))
    lst.sort()
    a, b, c = lst
    if a == 0 and b == 0 and c == 0:
        break
    result = ''

    if a**2 + b**2 == c**2:
        result = 'right'
    else:
        result = 'wrong'

    print(result)
    
