# 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다.
#  정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
import sys
import collections


def solve():
    X, Y = map(int, sys.stdin.readline().replace("\n", "").split(" "))
    box = []
    fresh = 0
    for _ in range(Y):
        box.append(sys.stdin.readline().replace("\n", "").split(" "))
    queue = collections.deque([])
    for a in range(Y):
        for b in range(X):
            if box[a][b] == "1":
                queue.append([a, b, 0])
            elif box[a][b] == "0":
                fresh += 1
    moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    while queue:
        ny, nx, day = queue.popleft()
        for move in moves:
            dy, dx = move
            if Y > ny+dy > -1 and X > nx+dx > -1 and box[ny+dy][nx+dx] == "0":
                box[ny+dy][nx+dx] = "1"
                fresh -= 1
                queue.append([ny+dy, nx+dx, day + 1])
    if fresh == 0:
        return day
    else:
        return -1


print(solve())
