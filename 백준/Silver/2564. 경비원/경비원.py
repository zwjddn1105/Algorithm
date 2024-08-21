n, m = map(int, input().split())
# 위치를 1자로 펴서 생각하기
sto_num = int(input())
store = []
for _ in range(sto_num):
    dir, dis = map(int, input().split())
    store.append([dir, dis])
don_dir, don_dis = map(int, input().split())

def real_dis(dir, dis):
    if dir == 1:
        return dis
    elif dir == 2:
        return n + m + n - dis
    elif dir == 3:
        return n*2 + m*2 - dis
    elif dir == 4:
        return n + dis
    
real_ddis = real_dis(don_dir, don_dis)
result = 0
for i in store:
    a = real_dis(i[0],i[1])
    b = (n*2 + m*2)
    calculate = min(abs(real_ddis-a), b-abs(real_ddis-a))
    result += calculate

print(result)