# import sys

# sys.stdin = open('4864_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    len_str1 = len(str1)
    len_str2 = len(str2)
    result = 0
    for i in range(len_str2-len_str1+1):
        if str1 == str2[i:(i+len_str1)]:
            result = 1

    print(f'#{tc} {result}')