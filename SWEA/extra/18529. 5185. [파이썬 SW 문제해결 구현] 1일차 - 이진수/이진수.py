#import sys

#sys.stdin = open('5185_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n, hexadecimal = map(str, input().split())
    n = int(n)

    info = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    info_lst = ['A', 'B', 'C', 'D', 'E', 'F']

    def change(num):
        num = int(num)
        binary = ''
        while num > 0:
            binary = str(num % 2) + binary
            num = num // 2
        if len(binary) == 3:
            binary = '0' + binary
        elif len(binary) == 2:
            binary = '00' + binary
        elif len(binary) == 1:
            binary = '000' + binary
        elif len(binary) == 0:
            binary = '0000'
        return binary

    print(f'#{tc}', end=' ')
    for i in range(n):
        if hexadecimal[i] in info_lst:
            number = info[hexadecimal[i]]
            print(change(number), end='')
        else:
            print(change(hexadecimal[i]), end='')
    print()