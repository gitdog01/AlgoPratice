import sys


def find(n, space, like):
    answers = [-1 - 1]
    ls = 0
    moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    for y in range(len(n)):
        for x in range(len(n)):
            temp = 0
            if space[y][x] == -1:
                for move in moves:
                    dy, dx = move
                    if n > y + dy > -1 and n > x + dx > -1 and space[y+dy][x+dx] != -1 and space[y+dy][x+dx] in like:
                        temp += 1
                if temp > ls:
                    answers = [y, x]
    return answers


def empty(n, space):
    answers = [-1 - 1]
    emptySpace = 0
    moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    for y in range(len(n)):
        for x in range(len(n)):
            temp = 0
            if space[y][x] == -1:
                for move in moves:
                    dy, dx = move
                    if n > y + dy > -1 and n > x + dx > -1 and space[y+dy][x+dx] == -1:
                        temp += 1
                if temp > emptySpace:
                    answers = [y, x]
    return answers


N = int(sys.stdin.readline().replace("\n", ""))
S = [[] for _ in range((N**2)+1)]
space = [[-1 for _ in range(N)] for _ in range(N)]
for _ in range(N**2):
    line = list(map(int, sys.stdin.readline().replace("\n", "").split()))
    S.append(line)


for one in S:
    ny, nx
    # 2,3
    ny, nx = empty(N, space)
    space[ny][nx] = one[0]


# 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
