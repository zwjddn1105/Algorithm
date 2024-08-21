w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

# 가로 방향 계산
x = (p+t) % (2*w)
if x > w:
    x = 2*w - x

# 세로 방향 계산
y = (q+t) % (2*h)
if y > h:
    y = 2*h - y

print(f'{x} {y}')
