n = int(input())
arr = [[0]*100 for _ in range(100)]
info = [tuple(map(int, input().split())) for _ in range(n)]

for i in info:
    a = i[0]
    b = i[1]
    c = 90-b
    for j in range(a, a+10):
        for k in range(c, c+10):
            arr[j][k] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j]:
            cnt += 1

print(cnt)