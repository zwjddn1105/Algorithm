# import sys

# sys.stdin = open('GNS_test_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n, m = map(str, input().split())
    data = list(map(str, input().split()))
    # temp = []
    # # 방법이 생각이 안나서 하나하나 조회해서 추가..
    # for i in range(0, len(data)):
    #     if data[i] == 'ZRO':
    #         temp.append(data[i])
    # for i in range(0, len(data)):
    #     if data[i] == 'ONE':
    #         temp.append(data[i])
    # for i in range(0, len(data)):
    #     if data[i] == 'TWO':
    #         temp.append(data[i])
    # for i in range(0, len(data)):
    #     if data[i] == 'THR':
    #         temp.append(data[i])
    # for i in range(0, len(data)):
    #     if data[i] == 'FOR':
    #         temp.append(data[i])
    # for i in range(0, len(data)):
    #     if data[i] == 'FIV':
    #         temp.append(data[i])
    # for i in range(0, len(data)):
    #     if data[i] == 'SIX':
    #         temp.append(data[i])
    # for i in range(0, len(data)):
    #     if data[i] == 'SVN':
    #         temp.append(data[i])
    # for i in range(0, len(data)):
    #     if data[i] == 'EGT':
    #         temp.append(data[i])
    # for i in range(0, len(data)):
    #     if data[i] == 'NIN':
    #         temp.append(data[i])

    # 카운팅 정렬 풀이
    lst = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    empty_dict = {'ZRO': 0, 'ONE': 0, 'TWO': 0, 'THR': 0, 'FOR': 0, 'FIV': 0, 'SIX': 0, 'SVN': 0, 'EGT': 0, 'NIN': 0}
    print(n)
    for i in data:
        empty_dict[i] += 1
    for i in lst:
        while empty_dict[i] != 0:
            empty_dict[i] -= 1
            print(i, end=' ')
    print()