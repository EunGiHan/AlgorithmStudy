n, m = map(int, input().split(' '))
d = [[0] * m for _ in range(n)]
x, y, dir = map(int, input().split())
d[x][y] = 1 # 가본곳과 가보지 않은 곳 저장

map = []    # 물인 곳과 육지인 곳 저장
for _ in range(n):
    map.append(list(map(int, input().split)))

# 북 - 동 - 남 - 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 1
turn = 0
while True:
    # 왼쪽 회전
    dir -= 1
    if dir == -1:
        dir = 3
    
    nx = x + dx[dir]
    ny = y + dy[dir]

    if d[nx][ny] == 0 and map[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn = 0
        continue
    else:
        turn += 1
    
    if turn == 4:   # 네 방향 모두 갈 수 없음
        nx = x - dx[dir]
        ny = y - dy[dir]
        if map[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn = 0

print(cnt)