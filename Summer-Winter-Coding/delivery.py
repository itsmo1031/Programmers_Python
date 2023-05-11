"""
Lv.2 - 배달
Link: https://school.programmers.co.kr/learn/courses/30/lessons/12978
"""
eN = 6
eroad = [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]]
eK = 4

graph = []
visited = []


def dfs(start, time, possible):
    possible.add(start)
    for d, t in graph[start]:
        if ({start, d}, time) not in visited and t <= time:
            visited.append(({start, d}, time))
            dfs(d, time - t, possible)
    return len(possible)


def solution(N, road, K):
    global graph
    graph = [[] for _ in range(N + 1)]
    for r in road:
        a, b, t = r
        graph[a].append((b, t))
        graph[b].append((a, t))
    answer = dfs(1, K, set())
    return answer


print(solution(eN, eroad, eK))
