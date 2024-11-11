#import sys

#sys.stdin = open('sample_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())

    def binary_search():
        start = 1
        end = n
        while start <= end:
            mid = (start+end) // 2
            if mid**3 == n:
                return mid
            elif mid**3 < n:
                start = mid + 1
            elif mid**3 > n:
                end = mid -1
        return -1

    a = binary_search()

    print(f'#{tc} {a}')
