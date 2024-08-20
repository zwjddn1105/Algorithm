N = int(input())
arr = list(map(int, input().split()))

# 오름차순과 내림차순 길이를 저장할 리스트
up = [1] * N
down = [1] * N

# 오름차순 계산
for i in range(1, N):
    if arr[i-1] <= arr[i]:
        up[i] = up[i-1] + 1

# 내림차순 계산
for i in range(1, N):
    if arr[i-1] >= arr[i]:
        down[i] = down[i-1] + 1

# 가장 긴 길이 구하기
result = max(max(up), max(down))

print(result)