"""
문제 분류: Greedy & Sorting
---
입력 배열을 오름차순으로 정렬.
가장 적게 시간이 걸리는 사람부터 돈을 뽑아야 대기시간이 최소가 됨.
"""

# 입력
N = int(input())  # 총 인원 수
p = input().split(' ')
p = [int(p_i) for p_i in p]  # 각 사람 별 걸리는 시간

# 정렬
p.sort() # 오름차순 정렬
p_i_time = [sum(p[:i+1]) for i in range(len(p))] # 최적의 경우에 각 사람이 걸리는 시간
print(sum(p_i_time)) # 총 대기 시간
