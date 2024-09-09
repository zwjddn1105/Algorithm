#import sys

#sys.stdin = open('sample_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n, w, h = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(h)]
    min_blocks = 1e9
    blocks = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j]:
                blocks += 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def shoot(level, remains, now_arr):
        global min_blocks
        if level == n or remains == 0:
            min_blocks = min(min_blocks, remains)
            return

        for col in range(w):
            copy_arr = [row[:] for row in now_arr]
            row = -1
            for r in range(h):
                if copy_arr[r][col]:
                    row = r
                    break
            if row == -1:
                continue
            li = [(row, col, copy_arr[row][col])]
            now_remains = remains - 1
            copy_arr[row][col] = 0

            while li:
                r, c, p = li.pop()
                for k in range(1, p):
                    for i in range(4):
                        nr = r + dy[i]*k
                        nc = c + dx[i]*k
                        if nr < 0 or nr >= h or nc < 0 or nc >= w:
                            continue
                        if copy_arr[nr][nc] == 0:
                            continue
                        li.append((nr, nc, copy_arr[nr][nc]))
                        copy_arr[nr][nc] = 0
                        now_remains -= 1
            for c in range(w):
                idx = h - 1
                for r in range(h-1, -1, -1):
                    if copy_arr[r][c]:
                        copy_arr[r][c], copy_arr[idx][c] = copy_arr[idx][c], copy_arr[r][c]
                        idx -= 1
            shoot(level+1, now_remains, copy_arr)


    shoot(0, blocks, arr)

    print(f'#{tc} {min_blocks}')