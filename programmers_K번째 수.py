"""
나의 풀이
"""
def solution(array, commands):
  answer = []
  for command in commands:
    new_array = array[command[0]-1:command[1]]
    for j in range(len(new_array)-1):
      for i in range(len(new_array)-1):
        if new_array[i]>new_array[i+1]:
          temp = new_array[i]
          new_array[i] = new_array[i+1]
          new_array[i+1] = temp
    print(new_array)
    answer.append(new_array[command[2]-1])
  return answer

"""
다른 사람의 풀이 : map 함수와 lambda 함수, 리스트의 sorted 기능을 사용
"""
def solution(array, commands):
  return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
