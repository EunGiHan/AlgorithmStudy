N = int(input())
move = input().split(' ')

now = [1, 1]    # 행, 열
for m in move:
    if m == 'L':
        if now[1] > 1:
            now[1] -= 1 
        else:
            continue
    elif m == 'R':
        if now[1] < N:
            now[1] += 1 
        else:
            continue
    elif m == 'U':
        if now[0] > 1:
            now[0] -= 1 
        else:
            continue
    elif m == 'D':
        if now[0] < N:
            now[0] += 1 
        else:
            continue
print(now[0], now[1])


### 정답
n = int(input())
x, y = 1, 1
plans = input().split

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
