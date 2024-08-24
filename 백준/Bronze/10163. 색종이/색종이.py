n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
arr = [[0]*1001 for _ in range(1001)]

# 색종이 n장
for i in range(n):
    left_down_x = data[i][0]
    left_down_y = data[i][1]
    hor_length = data[i][2]
    ver_length = data[i][3]
    for k in range(left_down_x, left_down_x + hor_length):
        for j in range(left_down_y, left_down_y + ver_length):
            arr[k][j] = i+1

p = 1
while p <= n:
    cnt = 0
    for i in range(1001):
        for j in range(1001):
            if arr[i][j] == p:
                cnt += 1
    print(cnt)
    p += 1