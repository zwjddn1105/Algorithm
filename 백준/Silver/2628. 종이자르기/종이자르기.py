n, m = map(int, input().split())
cut_num = int(input())
cut_style = [tuple(map(int, input().split())) for _ in range(cut_num)]

hor = [0] * (n+1)
h_cnt = 1
hor[0] = h_cnt

ver = [0] * (m+1)
v_cnt = 1
ver[0] = v_cnt

final_x = 0
final_y = 0

for i in cut_style:
    if i[0] == 0:
        v_cnt += 1
        ver[i[1]] = v_cnt
    elif i[0] == 1:
        h_cnt += 1
        hor[i[1]] = h_cnt

v_cnt += 1
ver[m] = v_cnt
h_cnt += 1
hor[n] = h_cnt

idx = []
for i in hor:
    if i:
        a = hor.index(i)
        idx.append(a)

for i in range(1, len(idx)):
    b = idx[i] - idx[i-1]
    final_x = max(final_x, b)

idx2 = []
for i in ver:
    if i:
        c = ver.index(i)
        idx2.append(c)

for i in range(1, len(idx2)):
    d = idx2[i] - idx2[i-1]
    final_y = max(final_y, d)

print(final_x*final_y)