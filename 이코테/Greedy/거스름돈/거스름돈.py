n = int(input())
count = 0

lst = [500, 100, 50, 10]
# idx = 0
# price = n
# while price > 0:
#     if price >= lst[idx]:
#         count += 1
#         price -= lst[idx]
#     else:
#         idx += 1

for coin in lst:
    count += n // coin
    n %= coin
    
print(count)
