import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

result = a*b*c
result = str(result)
num_dict = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
for i in result:
    num_dict[i] += 1

for i in num_dict.values():
    print(i)