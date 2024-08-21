n = int(input())
col = [tuple(map(int, input().split())) for _ in range(n)]
col.sort(key=lambda x:x[0])

x1 = col[0][1]
x2 = col[-1][1]

total = 0

top_high = max(col, key=lambda x:x[1])[1]
top_idx = max(list(enumerate(col)), key=lambda x: x[1][1])[0]

for i in range(top_idx):
    if x1 < col[i][1]:
        x1 = col[i][1]
    total += x1*(col[i+1][0] - col[i][0])


for i in range(n-1, top_idx, -1):
    if x2 < col[i][1]:
        x2 = col[i][1]
    total += x2*(col[i][0] - col[i-1][0])

total += top_high

print(total)