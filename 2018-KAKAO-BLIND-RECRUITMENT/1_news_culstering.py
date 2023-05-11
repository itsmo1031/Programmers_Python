# [1차] 뉴스 클러스터링
# 다중 집합을 리스트로 표현해야 하므로 set의 intersection/union 사용 불가능
# 직접 intersection과 union을 구현하여 계산

def jaccard(s1, s2):
    s1 = split(s1)
    s2 = split(s2)
    inter = len(intersection(s1, s2))
    uni = len(union(s1, s2))
    return inter / uni if uni != 0 else 1


def intersection(s1, s2):
    result = []
    s2 = s2.copy()
    for s in s1:
        if s in s2:
            s2.remove(s)
            result.append(s)
    return result


def union(s1, s2):
    result = s1 + s2
    for i in intersection(s1, s2):
        if i in result:
            result.remove(i)
    return result


def split(word):
    result = []
    for i in range(0, len(word) - 1):
        nw = word[i:i + 2]
        if nw.isalpha():
            result.append(nw.lower())
    return result


def solution(str1, str2):
    return int(jaccard(str1, str2) * 65536)

# solution("aa1+aa2", "AAAA12")
