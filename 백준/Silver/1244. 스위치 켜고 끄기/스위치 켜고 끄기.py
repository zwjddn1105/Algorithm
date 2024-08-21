n = int(input())
switch = list(map(int, input().split()))
switch.insert(0, -1)
stu = int(input())

def change(idx):
    global switch
    if switch[idx] == 1:
        switch[idx] = 0
    else:
        switch[idx] = 1
    return 

# 남자 1 여자 2
for _ in range(stu):
    seong, num = map(int, input().split())
    if seong == 1:
        for i in range(num, n+1, num):
            change(i)
    else:
        change(num)
        k = 1
        while True:
            x = num - k
            y = num + k
            if 0 < x < n+1 and 0 < y < n+1:
                if switch[x] == switch[y]:
                    change(x)
                    change(y)
                else:
                    break
            else:
                break
            k += 1

for i in range(1, n+1):
    if i % 20 != 0:
        print(switch[i], end=' ')
    else:
        print(switch[i])