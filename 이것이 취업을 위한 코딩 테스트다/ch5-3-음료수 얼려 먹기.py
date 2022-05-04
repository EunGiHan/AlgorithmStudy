import numpy as np

n, m = map(int, input().split())
mold = []
for _ in range(n):
    mold.append(list(map(int, input().split())))
visited = np.zeros_like(mold)

def dfs(row, col):
    if row < 0 or row > n or col < 0 or col > m:
        return False
    if mold[row][col] == 1:
        return False
    if visited[row][col] == True:
        return False

    visited[row][col] = True

    dfs(row - 1, col)
    dfs(row + 1, col)
    dfs(row, col - 1)
    dfs(row, col + 1)

    return True

cnt = 0
for row in range(n):
    for col in range(m):
        if dfs(row, col) == True:
            cnt += 1
print(cnt)