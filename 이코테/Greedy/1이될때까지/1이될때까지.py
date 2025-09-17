n, k = map(int, input().split())
count = 0

# 이건 n이 항상 k보다 크거나 같아서 가능함
while True:
    target = (n // k) * k
    count += (n - target)
    n = target
    if n < k:
        break
    count += 1
    n //= k

count += (n - 1)
print(count)