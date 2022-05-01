input_data = input()
col, row = input_data[0], int(input_data[1])
dx = [-1, 1, -1, 1, -2, -2, 2, 2]
dy = [2, 2, -2, -2, 1, -1, 1, -1]
col_num = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
col = col_num[col]

cnt = 0
for i in range(8):
    cx = col + dx[i]
    cy = row + dy[i]
    if cx < 1 or cx > 8 or cy < 1 or cy > 8:
        continue
    cnt += 1

print(cnt)


### 정답

input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]
    if next_row >= 1 or next_row <= 8 or next_col >= 1 or next_col <= 8:
        result += 1
print(result)