n = int(input())

star = '*'

for i in range(1, n+1):
    print(' '*(n-i), end='')
    print(star*i)