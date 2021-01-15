def bfs(board):
    visited = [[1000000 for _ in range(len(board))] for _ in range(len(board))]
    queue = [[0, 0, 0, 0], [0, 0, 0, 1]]
    answer = 1000000
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dd = [0, 1, 2, 3]
    count = 0
    while queue:
        y, x, direction, money = queue.pop(0)
        visited[y][x] = min(money, visited[y][x])
        for idx in range(4):
            nm = money
            ny = y + dy[idx]
            nx = x + dx[idx]
            nm += 100 if direction == dd[idx] else 600

            if ny == len(board) - 1 and nx == len(board) - 1:
                answer = min(nm, answer)
                visited[ny][nx] = answer
            elif len(board) > ny >= 0 and len(board) > nx >= 0 and visited[ny][nx] > nm and board[ny][nx] != 1:
                queue.append([ny, nx, dd[idx], nm])
                count += 1
    print(count)
    return answer


def solution(board):
    return min(bfs(board))


print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
