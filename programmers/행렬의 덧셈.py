# link for problem : https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    return [[sum(row) for row in zip(*matrix)] for matrix in zip(arr1, arr2)]
