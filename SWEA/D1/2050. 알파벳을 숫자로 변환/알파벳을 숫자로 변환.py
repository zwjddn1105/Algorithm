# import sys

# sys.stdin = open('input.txt')


alphabet = list(input().split())
data = alphabet[0]

for i in data:
    result = int(ord(i))-64
    print(result, end=' ')
