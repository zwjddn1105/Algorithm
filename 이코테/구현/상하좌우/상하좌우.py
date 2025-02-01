n = int(input())
move = input().split()

start = [0,0]
for m in move:
    if m == 'R':
        if start[1] == n-1:
            continue
        start[1] += 1
    elif m == 'L':
        if start[1] == 0:
            continue
        start[1] -= 1
    elif m == 'U':
        if start[0] == 0:
            continue
        start[0] -= 1
    elif m == 'D':
        if start[0] == n-1:
            continue
        start[0] += 1
x = start[0] + 1
y = start[1] + 1
print(x, y)