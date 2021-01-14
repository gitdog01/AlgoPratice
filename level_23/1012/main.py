def search(visited, arr, x, y):
    count = 0
    queue = [[y, x]]
    move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    while len(queue) != 0:
        ny, nx = queue.pop()
        if arr[ny][nx] != 0 and visited[ny][nx] != True:
            count += 1
            visited[ny][nx] = True
            for dy, dx in move:
                if -1 < ny+dy < len(visited) and -1 < nx+dx < len(visited[0]):
                    if visited[ny+dy][nx+dx] != True and arr[ny+dy][nx+dx] != 0:
                        queue.append([ny+dy, nx+dx])
    return count


n = int(input())
numbers = []
for _ in range(n):
    fx, fy, bea = map(int, input().split(' '))
    field = [[0 for _ in range(fx)] for _ in range(fy)]
    visited = [[False for _ in range(fx)] for _ in range(fy)]
    result = []
    for _ in range(bea):
        x, y = map(int, input().split(' '))
        field[y][x] = 1

    for ny in range(fy):
        for nx in range(fx):
            if visited[ny][nx] != True and field[ny][nx] != 0:
                result.append(search(visited, field, nx, ny))
    numbers.append(len(result))
for number in numbers:
    print(number)
