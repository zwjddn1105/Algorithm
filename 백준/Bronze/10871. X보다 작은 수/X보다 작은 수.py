import sys
input = sys.stdin.readline

N, X = map(int, input().split())
arr = list(map(int, input().split()))

for i in arr:
    if i < X:
        print(i, end=' ')