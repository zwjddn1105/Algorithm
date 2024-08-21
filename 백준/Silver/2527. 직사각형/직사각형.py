'''
8개 데이터 주어지면 4개씩 끊어서 직사각형 좌표인데 두 직사각형이 
아예 따로 노는지, 점인지, 선분인지, 겹치는지 d c b a
좌표기준으로 생각해서 구하기, 굳이 2차원배열 안 만들어도 됨
'''

def check(r1, r2):
    x1, y1, p1, q1 = r1
    x2, y2, p2, q2 = r2
    
    if p1 < x2 or p2 < x1 or q1 < y2 or q2 < y1:
        return 'd'
    
    if (p1 == x2 and q1 == y2) or (x1 == p2 and q1 == y2) or (p1 == x2 and y1 == q2) or (x1 == p2 and y1 == q2):
        return 'c'

    if y1 == q2 and not (p1 < x2 or p2 < x1):
        return 'b'

    if q1 == y2 and not (p1 < x2 or p2 < x1):
        return 'b'

    if p1 == x2 and not (q1 < y2 or q2 < y1):
        return 'b'
  
    if x1 == p2 and not (q1 < y2 or q2 < y1):
        return 'b'
 
    return 'a'

for _ in range(4):
    data = list(map(int, input().split()))
    r1 = data[:4]
    r2 = data[4:]
    print(check(r1, r2))
