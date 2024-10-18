lst = set()

for _ in range(10):
    num = int(input())
    num2 = num % 42
    lst.add(num2)

print(len(lst))