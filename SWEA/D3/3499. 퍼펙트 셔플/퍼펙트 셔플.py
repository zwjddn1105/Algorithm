T = int(input())
for tc in range(1, T+1):
    n = int(input())
    card = input().split()
    deck = [0]*n

    d = (n+1) // 2     # 아래 카드 시작인덱스
    i1 = 0
    i2 = d
    deck_idx = 0          # 새로 만들 덱의 인덱스
    while deck_idx < n:
        if i1 < d:
            deck[deck_idx] = card[i1]
            i1 += 1
            deck_idx += 1
        if i2 < n:
            deck[deck_idx] = card[i2]
            i2 += 1
            deck_idx += 1

    print(f'#{tc}', *deck)