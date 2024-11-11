#import sys
#sys.stdin = open('input.txt')

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(100)]
    empty = [[0]*100 for _ in range(100)]
    # 세로 배열 만들기
    for i in range(100):
        for j in range(100):
            empty[i][j] = arr[j][i]
    result = []
    for i in range(100):
        for j in range(100):
            for k in range(100-j,0,-1):
                h_word = arr[i][j:j+k]
                re_h_word = h_word[::-1]
                if h_word == re_h_word:
                    result.append(len(h_word))
                    break
    for i in range(100):
        for j in range(100):
            for k in range(100-j,0,-1):
                v_word = empty[i][j:j+k]
                re_v_word = v_word[::-1]
                if v_word == re_v_word:
                    result.append(len(v_word))
                    break               

    answer = result[0]
    for i in range(len(result)):
        if answer < result[i]:
            answer = result[i]
   
    print(f'#{n} {answer}')