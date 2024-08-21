'''
빙고가 나올 수 있는 모든 경우의 수를 함수로 만들어서 했지만..
그냥 델타검색으로 해도 될 것 같음
'''
me = [list(map(int, input().split())) for _ in range(5)]
you = [list(map(int, input().split())) for _ in range(5)]


def change(a):
    for i in range(5):
        for j in range(5):
            if me[i][j] == a:
                me[i][j] = 0

def counts1():
    p = 0
    for i in range(5):
        if me[i][i] == 0:
            p += 1
    if p == 5:
        return 1
    return False

def counts2():
    p = 0
    for i in range(5):
        if me[i][4 - i] == 0:
            p += 1
    if p == 5:
        return 1
    return False

def counts3():
    j = 0
    bingo = 0
    while j < 5:
        p = 0
        for i in range(5):
            if me[i][j] == 0:
                p += 1
        if p == 5:
            bingo += 1
        j += 1
    asd = bingo
    return asd

def counts4():
    j = 0
    bingo = 0
    while j < 5:
        p = 0
        for i in range(5):
            if me[j][i] == 0:
                p += 1
        if p == 5:
            bingo += 1
        j += 1
    asd = bingo
    return asd


cnt = 0
result = True
for i in range(5):
    if result:
        for j in range(5):
            a = you[i][j]
            change(a)
            cnt += 1
            if counts1() + counts2() + counts3() + counts4() >= 3:
                print(cnt)
                result = False
                break