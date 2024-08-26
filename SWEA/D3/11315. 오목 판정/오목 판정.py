'''
델타검색으로 오목알 연속으로 5개있는 위치 찾기
중간에 오목알 없으면 중단!
이거 함수 다 따로만들면 대각선일 때 머리아파짐.. 델타검색으로 한 번에 하는 게 낫다
'''
#import sys

#sys.stdin = open('sample_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(str, input())) for _ in range(n)]

    dx = [1, -1, 0, 0, -1, -1, 1, 1]    # 8방향
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    def omok():
        for i in range(n):
            for j in range(n):
                if arr[i][j] == 'o':
                    for k in range(8):
                        cnt = 1
                        for l in range(1,6):
                            nx = i + dx[k]*l
                            ny = j + dy[k]*l
                            if 0 <= nx < n and 0 <= ny < n:
                                if arr[nx][ny] == 'o':
                                    cnt += 1
                                else:
                                    break
                                if cnt == 5:
                                    return True

    if omok():
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')