# import sys

# sys.stdin = open('4865_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    lst_str1 = list(map(str, input()))
    lst_str2 = list(map(str, input()))
    dict_str2 = {}

    for i in lst_str2:
        dict_str2.setdefault(i, False)
        dict_str2[i] += 1

    result = dict_str2[lst_str1[0]]
    for j in lst_str1:
        if result < dict_str2[j]:
            result = dict_str2[j]

    print(f'#{tc} {result}')