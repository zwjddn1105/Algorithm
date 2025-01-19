n,m,k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort(reverse=True)
num1 = numbers[0]
num2 = numbers[1]

# count_m = 0
# count_k = 0
# result = 0
# while True:
#     if count_m == m:
#         break
#     result += num1
#     count_m += 1
#     count_k += 1
#     if count_k == k:
#         count_k = 0
#         result += num2
#         count_m += 1
result = 0
# 가장 큰 수가 더해지는 횟수
count = int(m / (k+1)) * k
count += m % (k+1)

result += count * num1
result += (m-count) * num2
print(result)