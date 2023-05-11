# [1차] 캐시 - Lv.2
# https://school.programmers.co.kr/learn/courses/30/lessons/17680

from collections import deque


def solution(cacheSize, cities):
    answer = 0
    # deque의 maxlen option을 활용하면 과정을 더 줄일 수 있다.
    cache = deque()
    for city in cities:
        city = city.lower()
        answer += 1 if city in cache else 5
        if city in cache:
            cache.remove(city)
            cache.appendleft(city)
        else:
            if cacheSize == 0:
                continue
            if len(cache) == cacheSize:
                cache.pop()
            cache.appendleft(city)
    return answer
