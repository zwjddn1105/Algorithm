data = [list(map(int, input().split())) for _ in range(4)]
arr = [[0]*101 for _ in range(101)]
cnt = 0
for i in range(4):
    rec1_x = data[i][0]
    rec1_y = data[i][1]
    rec2_x = data[i][2]
    rec2_y = data[i][3]
    for j in range(rec1_x, rec2_x):
        for k in range(rec1_y, rec2_y):
            arr[j][k] = 1

for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)