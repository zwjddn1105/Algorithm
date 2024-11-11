#import sys

#sys.stdin = open('sample_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    synergy = [list(map(int, input().split())) for _ in range(n)]
    material = list(range(n))

    case = []
    path = []
    def combination(level, start):
        if level == n//2:
            tra = []
            for i in material:
                if i not in path:
                    tra.append(i)
            case.append(path[:]+tra)
            return
        for i in range(start, n):
            path.append(material[i])
            combination(level+1, i+1)
            path.pop()
    combination(0,0)

    result = float('inf')
    for i in range(len(case)//2):
        mat_a = case[i][:n//2]
        mat_b = case[i][n//2:]
        taste_a = 0
        taste_b = 0
        for j in mat_a:
            for k in mat_a:
                taste_a += synergy[j][k]

        for j in mat_b:
            for k in mat_b:
                taste_b += synergy[j][k]
        ans = abs(taste_a - taste_b)
        result = min(result, ans)
    print(f'#{tc} {result}')