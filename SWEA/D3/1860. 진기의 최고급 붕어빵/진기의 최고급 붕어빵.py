#import sys

#sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):
    n, m, k = map(int, input().split())  # n명의 사람 m초에 k개 생성가능
    visit_time = list(map(int, input().split()))
    visit_time.sort()

    # 시작은 0초부터 만들기 시작
    carp = 0  # 붕어
    time = 0

    for i in range(n):
        while time < visit_time[i]:
            time += 1
            if time % m == 0:
                carp += k
        if carp < 1:
            result = False
            break
        else:
            carp -= 1
            result = True

    if result == True:
        print(f'#{tc} Possible')
    elif result == False:
        print(f'#{tc} Impossible')
