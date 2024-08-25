'''
그냥 문제 그대로 코드 만들어서 노가다 뛰었음
'''
T = range(1, 11)

for j in T:
    N = int(input())
    High = list(map(int, input().split()))
    result = 0
    for i in range(2, len(High)-2):
        if High[i] > High[i-2] and High[i] > High[i-1] and High[i] > High[i+1] and High[i] > High[i+2]:
            lst = [-1, 1, 2]
            k = High[i - 2]
            for q in lst:
                if k - High[i+q] < 0:
                    k = High[i+q]

            result += High[i] - k

    print(f'#{j} {result}')