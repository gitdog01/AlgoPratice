import sys


def find(paper, y, x, count):
    if count == 4:
        return
    moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    for move in moves:
        dy, dx = move


N, M = map(int, sys.stdin.readline().replace("\n", "").split(" "))
answer = 0
paper = []
for _ in range(N):
    paper.append(sys.stdin.readline().replace("\n", "").split(" "))

for y in range(N):
    for x in range(M):
        answer = max(find(paper, y, x, 0), answer)
print(answer)
