import math

"""
나의 풀이
"""
def solution(brown, yellow):
  answer = []
  for i in range(1, int(math.sqrt(yellow))+1):
    row = float(yellow/i)
    col = i
    if row.is_integer and brown==(2*col+2*row+4):
      answer = [int(row+2), col+2]
      break
  return answer


"""
다른 사람의 풀이 : 길이와 넓이 2개의 식 -> 2차방정식 -> 근의 공식 이용
"""
def solution(braown, yellow):
  width = ((brown+4)/2 + math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
  height = ((brown+4)/2 - math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
  return [width, height]
