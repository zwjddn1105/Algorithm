num_lst = []

p = 0
b = 0

for i in range(9):
    a = int(input())
    num_lst.append(a)

for j in range(9):
    if num_lst[j] > p:
        p = num_lst[j]
        b = j+1

print(p)
print(b)