# 전형적인 파라메트릭 서치 유형의 문제 (Parametric Search)
# 범위 내에서 조건을 만족하는 가장 큰 값을 찾으라는 최적화 문제
# 원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제
# 큰 수를 보면 당연하다는 듯이 이진탐색을 떠올릴 것

import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
ricecakes = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(ricecakes)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in ricecakes:
        if i > mid:
            total += i-mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)