import sys
n = int(sys.stdin.readline().rstrip())
dongbin = list(map(int, sys.stdin.readline().rstrip().split()))
dongbin.sort() # 정렬 까먹지말고 꼭 하기
m = int(sys.stdin.readline().rstrip())
customer = list(map(int, sys.stdin.readline().rstrip().split()))

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None

for product in customer:
    if binary_search(dongbin, product, 0, n-1):
        print('yes', end=' ')
    else:
        print('no', end=' ')


# 이 문제는 카운트정렬이랑 set()함수로 풀 수도 있음. in을 써서 풀수도 있을 듯