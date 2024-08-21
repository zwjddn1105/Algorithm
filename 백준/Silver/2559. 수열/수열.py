'''
연속된 날짜 k동안 나올 수 있는 온도합 최대값 구하기
누적합 이용하는 것이 가장 시간초 짧고 효율적
'''
n, k = map(int, input().split())
data = list(map(int, input().split()))

arr = [0]*(n-k+1)
arr[0] = sum(data[:k])

for i in range(1, n-k+1):
    arr[i] = arr[i-1] - data[i-1] + data[i-1+k]

print(max(arr))