#import sys
 
#sys.stdin = open('sample_input.txt')
 
# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
 
    dx = [1, 1, -1, -1] # 시계방향
    dy = [1, -1, -1, 1]
    route = []
 
    def explore(x, y, start_x, start_y, direction, lst):
        if direction == 4:
            return
 
        nx = x + dx[direction]
        ny = y + dy[direction]
        if (nx, ny) == (start_x, start_y) and len(lst) >= 4:    # 사각형이 만들어 지면
            route.append(lst[:])
            return
 
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] not in lst:
            lst.append(arr[nx][ny])
            explore(nx, ny, start_x, start_y, direction, lst)
            explore(nx, ny, start_x, start_y, direction + 1, lst)
            lst.pop()   # 꼭지점 갔다가 돌아오는 경우 때문에
 
 
    for i in range(n):
        for j in range(1,n-1):
            explore(i, j, i, j, 0, [arr[i][j]])
 
    if len(route) > 0:
        answer = max(len(i) for i in route)
        print(f'#{tc} {answer}')
    else:
        print(f'#{tc} -1')