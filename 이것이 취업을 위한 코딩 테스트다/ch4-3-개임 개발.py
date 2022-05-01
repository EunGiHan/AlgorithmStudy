n, m = map(int, input().split(' '))
a, b, d = map(int, input().split(' '))
map = []
for _ in range(n):
    row = list(map(int, input().split(' ')))
    map.append(row)
print(map)

dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
heading = d
cnt = 1

while True:
    for i in range(4):
        cx = a + dir[(heading - i) % 4][0]
        cy = b + dir[(heading - i) % 4][1]
        if map[cx, cy] == 0:
            cnt += 1
            map[cx, cy] = 2 # 가본 칸
            a, b = cx, cy
            heading = (heading - i + 1) % 4
            break
        else:
            continue
    if i == 3:
        cx = a + dir[(heading + 2) % 4][0]
        cy = b + dir[(heading + 2) % 4][1]
        if map[cx, cy] == 1:
            break
        else:
            map[cx, cy] = 2
            a, b = cx, cy
