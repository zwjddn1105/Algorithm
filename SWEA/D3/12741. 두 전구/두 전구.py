# 테케 50000개
# 결과를 저장해서 한번에 출력하기
#import sys

#sys.stdin = open('sample_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
ans = []
for tc in range(1, T+1):
    a, b, c, d = map(int, input().split())
    start = max(a,c)
    end = min(b,d)

    result = end - start

    if result < 0:
        ans.append(f'#{tc} 0')
    else:
        ans.append(f'#{tc} {result}')

for i in ans:
    print(i)