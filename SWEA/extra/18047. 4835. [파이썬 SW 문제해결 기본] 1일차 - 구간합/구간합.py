T = int(input())
for j in range(1, T+1):
    N, M = map(int, input().split())
    number = list(map(int, input().split()))
    empty_list = []

    for i in range(len(number)-M+1):
        a = 0
        count = 0
        while count < M:
            a += number[i]
            i += 1
            count += 1
        empty_list.append(a)

    for k in range(len(empty_list)-1):
        for q in range(len(empty_list)-k-1):
            if empty_list[q] > empty_list[q+1]:
                empty_list[q], empty_list[q+1] = empty_list[q+1], empty_list[q]

    result = empty_list[-1] - empty_list[0]

    print(f'#{j} {result}')