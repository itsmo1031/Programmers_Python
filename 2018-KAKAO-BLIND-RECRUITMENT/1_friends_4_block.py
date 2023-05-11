# [1차] 프렌즈4블록 - Lv.2


target = set()


def check(pos, board):
    x, y = pos
    if board[x][y] and board[x][y] == board[x + 1][y] == board[x][y + 1] == board[x + 1][y + 1]:
        target.update([(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)])


def boom(board):
    cnt = 0
    for x, y in target:
        if board[x][y]:
            board[x][y] = None
            cnt += 1
    return cnt


def drop(board):
    flip = [*map(list, zip(*board))]
    result = []
    for f in flip:
        cnt = f.count(None)
        nf = [None] * cnt + [*filter(None, f)]
        result.append(nf)
    return [*map(list, zip(*result))]


def solution(m, n, board):
    answer = 0
    nb = [[w for w in b] for b in board]
    while True:
        target.clear()
        for i in range(m - 1):
            for j in range(n - 1):
                check((i, j), nb)
        if len(target) == 0:
            break
        answer += boom(nb)
        nb = drop(nb)
    return answer


data = [[4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]],
        [6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]],
        [2, 2, ["TT", "TT"]]]

for d in data:
    M, N, B = d
    print(solution(M, N, B))
