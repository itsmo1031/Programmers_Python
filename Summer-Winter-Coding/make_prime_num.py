"""
Lv.1 = 소수 만들기
Link: https://school.programmers.co.kr/learn/courses/30/lessons/12977
"""
from itertools import combinations


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    for group in combinations(nums, 3):
        if is_prime(sum(group)):
            answer += 1
    return answer
