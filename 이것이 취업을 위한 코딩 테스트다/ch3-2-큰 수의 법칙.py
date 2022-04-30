n, m, k = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

arr.sort(reverse=True)

sum = 0
cnt = 0

# ### 개선 전
# for i in range(m):
#     if cnt >= 3:
#         sum += arr[1]
#         cnt = 0
#     else:
#         sum += arr[0]
#         cnt += 1

### 개선 후
cnt = (m // (k + 1)) * k + (m % (k + 1))
sum += cnt * arr[0]
sum += (m - cnt) * arr[1]

print(sum)