"""
Lv.1 - 예산
Link: https://school.programmers.co.kr/learn/courses/30/lessons/12982
"""


def solution(d, budget):
    answer = 0
    for k in sorted(d):
        if budget < k:
            break
        budget -= k
        answer += 1
    return answer
