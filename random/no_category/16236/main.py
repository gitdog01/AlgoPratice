import sys
import collections


def find_feed(array, size, n):
    answers = []

    for y in range(n):
        for x in range(n):
            if array[y][x] != 0 and array[y][x] < size:
                answers.append([y, x, 0])

    return answers


N = int(sys.stdin.readline().replace("\n", ""))
sea = []
for y in range(N):
    line = list(map(int, sys.stdin.readline().replace("\n", "").split()))
    if line.count(9) > 0:
        start_y = y
        start_x = line.index(9)
size = 2
hungry = 0
answer = 0
moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]
while True:

    # 찾아가기
    now_feed = find_feed(sea, size, N)
    queue = collections.deque([start_y, start_x, 0])
    while queue:
        ny, nx, nd = queue.pop()

        for move in moves:
            dy, dx = move
            if N > ny+dy > -1 and N > nx+dx > -1 and size > sea[ny+dy][nx+dx]:
                queue.append([ny+dy, nx+dx, nd+1])


print(answer)
