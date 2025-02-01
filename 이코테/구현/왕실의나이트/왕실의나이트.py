location = input()

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

x = range(97, 105)
y = range(1, 9)

count = 0

start_x = ord(location[0])
start_y = int(location[1])

for i in range(8):
    nx = start_x + dx[i]
    ny = start_y + dy[i]
    if nx in x and ny in y:
        count += 1
print(count)