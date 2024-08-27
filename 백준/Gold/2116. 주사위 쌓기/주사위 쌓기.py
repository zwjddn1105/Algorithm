'''
주사위 옆면의 합의 최대값, 맨아랫면을 결정하면 그 윗면, 다음주사위의 아래,윗면 모두 다 자동으로 결정됨 첫 주사위의 아랫면일 때 나올 수 있는 
최대값을 계산, 6번만 돌면 됨!
'''
n = int(input())
# 마주보는 주사위는 (A,F) (B,D) (C,E)
dice = [list(map(int, input().split())) for _ in range(n)]
idx = 0
result = 0    # 옆면의 합을 담을 결과

def updown_idx(i):    # 맨 아랫면인덱스에 따라 윗면의 인덱스 결정하는 함수
    if i == 0:
        return 5
    elif i == 1:
        return 3
    elif i == 2:
        return 4
    elif i == 3:
        return 1
    elif i == 4:
        return 2
    elif i == 5:
        return 0
    
for i in range(6):
    down = dice[0][i]    # 첫 주사위의 아랫면 결정
    up = dice[0][updown_idx(i)]    # 그에따라 자동 윗면 결정
    # 리스트 컴프리헨션 사용, enumerates는 인덱스값 포함한 튜플로 반환
    # 위아래면을 제외한 나머지 4개숫자 중 최대값을 계산
    total = max([value for (idx, value) in enumerate(dice[0]) if idx != i if idx != updown_idx(i)])

    for j in range(1, n):    # 나머지 주사위들
        down_idx = dice[j].index(up)    # 다음주사위 아랫면 인덱스는 그 전 주사위의 up값이 있는 인덱스
        up_idx = updown_idx(down_idx)    # 똑같이 윗면 인덱스 자동결정
        total += max([value for (idx, value) in enumerate(dice[j]) if idx != down_idx if idx != up_idx])
        up = dice[j][up_idx]    # 이걸 반드시 할당 해줘야 for문이 돌음
    
    result = max(result, total)    # 최대값 업데이트

print(result)
# 처음에 백트래킹이라 생각해서 재귀로 풀어보았으나 메모리초과, 재귀는 너무 많이 돌 것 같으면 쓰지말자