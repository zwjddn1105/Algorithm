#import sys

#sys.stdin = open('input.txt')

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    length = int(input())
    arr = [list(map(str, input().split())) for _ in range(8)]
    palindrome = 0
    for i in range(8):
        for j in range(8-length+1):
            word = arr[i][0][j:j+length]
            re_word = word[::-1]
            if word == re_word:
                palindrome += 1

    for i in range(8):
        word = ''
        for j in range(8):
            word += arr[j][0][i]
        for k in range(8-length+1):
            new_word = word[k:k+length]
            new_re_word = new_word[::-1]
            if new_word == new_re_word:
                palindrome += 1
    print(f'#{tc} {palindrome}')