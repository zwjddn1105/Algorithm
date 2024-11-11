from collections import deque
#import sys

#sys.stdin = open('sample_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n, m = map(int, input().split())

    visited = [0] * 1000001
    q = deque()
    q.append((n,0)) # 현재숫자, 현재연산횟수
    visited[n] = True

    def bfs():
        while q:
            now_number, cnt = q.popleft()
            if now_number == m:
                return cnt
            a = now_number + 1
            b = now_number * 2
            c = now_number - 1
            d = now_number - 10
            lst = [a, b, c, d]
            for num in lst:
                if num > 0:
                    if num <= 1000000:
                        if not visited[num]:
                            q.append((num, cnt + 1))
                            visited[num] = True

    result = bfs()
    print(f'#{tc} {result}')