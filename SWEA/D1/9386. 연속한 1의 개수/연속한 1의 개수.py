#import sys
 
#sys.stdin = open('input.txt')
 
# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N = input()
    list_arr = list(map(int, input()))
    empty_list = []
    count = 0
    for i in range(len(list_arr)):
        if i == 9 and list_arr[i] == 1:
            count += 1
            empty_list.append(count)
        elif list_arr[i] == 0:
            empty_list.append(count)
            count = 0
        elif list_arr[i] == 1:
            count += 1
 
    max_value = empty_list[0]
    for i in empty_list:
        if max_value < i:
            max_value = i
 
    print(f'#{tc} {max_value}')