"""
나의 풀이
"""
def solution(lottos, win_nums):
  lottos = list(filter(lambda x : x!=0, sorted(lottos)))
  correct = len([num for num in lottos if num in sorted(win_nums)])
  answer = [correct + (6-len(lottos)), correct]
  return list(map(lambda c : 7-c if c>=2 else 6, answer))


"""
다른 사람의 풀이(1) : cont() 함수 사용
"""
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
  

"""
다른 사람의 풀이(2) : dictionary와 set() 함수, & 연산자 사용
"""
def solution(lottos, win_nums):
    rank = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]
