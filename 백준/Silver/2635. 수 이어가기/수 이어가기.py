first = int(input())
final = []

for i in range(first, -1, -1):
    lst = [first, i]
    while True:
        x = lst[-2] - lst[-1]
        if x >= 0:
            lst.append(x)
        else:
            break

    if len(lst) > len(final):
        final = lst

print(len(final))
for i in final:
    print(i, end=' ')