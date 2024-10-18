n = int(input())

for _ in range(n):
    string = input()
    result = 0
    cnt = 0
    for i in string:
        if i == 'O':
           cnt += 1
           result += cnt
        else:
            cnt = 0
    print(result)