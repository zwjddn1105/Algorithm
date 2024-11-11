#import sys
#sys.stdin = open('5203_input.txt')

# Testcase 수
#Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    card = list(map(int, input().split()))
    p1 = [0]*10
    p2 = [0]*10

    result = 0
    flag = False
    for i in range(0, len(card), 2):
        c1, c2 = card[i], card[i+1]
        p1[c1] += 1
        p2[c2] += 1

        # 3개 연속 1이상인 인덱스가 발생하는 경우
        # 3개 이상 count 된 인덱스가 발생하는 경우
        for a in range(1, len(p1)-1):
            if p1[a-1] >= 1 and p1[a] >= 1 and p1[a+1] >= 1:
                result = 1
                flag = True
                break
        if flag:
            break
        for b in range(len(p1)):
            if p1[b] >= 3:
                result = 1
                flag = True
                break
        if flag:
            break
        for a in range(1, len(p2) - 1):
            if p2[a - 1] >= 1 and p2[a] >= 1 and p2[a + 1] >= 1:
                result = 2
                flag = True
                break
        if flag:
            break
        for b in range(len(p2)):
            if p2[b] >= 3:
                result = 2
                flag = True
        if flag:
            break

    if flag == False:
        print(f'#{tc} {0}')
    else:
        print(f'#{tc} {result}')