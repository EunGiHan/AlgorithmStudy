n, k = map(int, input().split(' '))

cnt = 0
while n != 1:
    if n % k == 0:
        n /= k
    else:
        n -= 1
    cnt += 1
print(cnt)

# ### 책 답안(1)
# cnt = 0
# while n >= k:
#     while n % k == 0:
#         cnt += 1
#         n -= 1
#     n //= k
#     cnt += 1
# while n > 1:
#     n -= 1
#     cnt += 1
# print(cnt)

### 책 답안(2)
# cnt = 0

# while True:
#     target = (n // k) * k   # 나누어 떨어지는 수
#     cnt += (n - target) # 나누어 떨어지는 수가 될때까지 1을 뺀 횟수
#     n = target  # 1씩 다 뺀 뒤 남은 수
#     if n < k:
#         break
#     n //= k
#     cnt += 1

# cnt += (n - 1)
# print(cnt)
