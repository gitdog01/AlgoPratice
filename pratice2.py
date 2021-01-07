# direction = { '동':0, '서':1, '남':2, '북':3}
def bfs(direct, start, board):
    visited = [[False for _ in len(range(board))] for _ in len(range(board))]
    queue = list([start[0], start[1], direct, 0])
    answer = int('inf')
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dd = [0, 2, 1, 3]
    while queue:
        y, x, direction, money = queue.pop(0)
        visited[y][x] = True
        for idx in range(4):
            ny = y + dy[idx]
            nx = x + dx[idx]
            money += 100 if direction == dd[idx] else 600
            direction = dd[idx]
            if ny == len(board) - 1 and nx == len(board) - 1:
                answer = min(answer, money)

            if len(board) > ny > 0 and len(board) > nx > 0 and answer < money and visited[ny][nx] == False:
                queue.append([ny, nx, direction, money])
    return answer


def solution(board):
    return min(bfs(0, [0, 0], board), bfs(2, [0, 0], board))
