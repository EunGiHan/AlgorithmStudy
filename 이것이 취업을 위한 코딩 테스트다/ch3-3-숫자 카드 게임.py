n, m = map(int, input().split(' '))
arr = []
for i in range(n):
    arr.append(list(map(int, input().split(' '))))

min_val = [min(row) for row in arr]
min_row_idx = min_val.index(max(min_val))

print(min_val[min_row_idx])

### 책 답안
# n, m = map(int, input().split(' '))
# result = 0
# for _ in range(n):
#     data = list(map(int, input().split(' ')))
#     min_val = min(data)
#     result = max(result, min_val)
# print(result)