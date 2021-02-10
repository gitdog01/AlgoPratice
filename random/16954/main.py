import sys
import collections

moves = [[0, 1], [1, 1], [1, 0], [0, -1],
         [-1, 0], [-1, -1], [1, -1], [-1, 1], [0, 0]]

# visited 를 추가하고 안하고 어떤 차이지 ??
# DFS 로 했으면 빠를까 ?


def bfs(b):

    queue = collections.deque([[7, 0]])
    while queue:
        visited = [[False] * 8 for _ in range(8)]
        q = len(queue)
        for _ in range(q):
            y, x = queue.popleft()
            if b[y][x] == '#':
                continue
            if y == 0 and x == 7:
                return 1
            for move in moves:
                dy, dx = move
                if (8 > y+dy > -1) and (8 > x+dx > -1) and b[y+dy][x+dx] != '#' and b[y][x] != '#' and visited[y+dy][x+dx] == False:
                    queue.append([y+dy, x+dx])
                    visited[y+dy][x+dx] = True
        b.pop()
        b.appendleft(list("........"))
    return 0


board = []
for _ in range(8):
    board.append(list(sys.stdin.readline().replace("\n", "")))
board = collections.deque(board)
print(bfs(board))
