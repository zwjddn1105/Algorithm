c, r = map(int, input().split())
k = int(input())
if k > c*r:
    print(0)
elif k == 1:
    print(f'1 1')
else:
    arr = [[0]*r for _ in range(c)]
    dx = [0, 1, 0, -1]      # 우 하 좌 상
    dy = [1, 0, -1, 0]
    direction = 0

    start_x = 0
    start_y = 0

    result_x = 0
    result_y = 0

    num = 1
    arr[start_x][start_y] = num

    while num <= k:
        nx = start_x + dx[direction]
        ny = start_y + dy[direction]
        if 0 <= nx < c and 0 <= ny < r and arr[nx][ny] == 0:
            num += 1
            arr[nx][ny] = num
            start_x = nx
            start_y = ny
        else:
            direction = (direction+1) % 4
        if num == k:
            result_x = nx+1
            result_y = ny+1
            break

    print(f'{result_x} {result_y}')