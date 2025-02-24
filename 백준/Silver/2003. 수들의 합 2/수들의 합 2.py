n, m = map(int, input().split())
arr = list(map(int, input().split()))
length = len(arr)
count = 0

for i in range(length):
    num = arr[i]
    if num == m:
        count += 1
        continue
    for j in range(i+1, length):
        num += arr[j]
        if num == m:
            count += 1
            break
        if num > m:
            break
print(count)
