n, k = map(int, input().split())
arr = [[] for _ in range(7)]
for _ in range(n):
    s, y = map(int, input().split())
    arr[y].append(s)
    arr[y].sort()

room = 0

for i in range(1,7):
    cnt_0 = 0
    cnt_1 = 0
    for j in arr[i]:
        if j == 0:
            cnt_0 += 1
        else:
            cnt_1 += 1
    if cnt_0 % k == 0:  
        room += cnt_0//k
    else:
        room += (cnt_0//k) + 1
    if cnt_1 % k == 0:  
        room += cnt_1//k
    else:
        room += (cnt_1//k) + 1

print(room)