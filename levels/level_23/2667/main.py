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
                if -1 < ny+dy < len(visited) and -1 < nx+dx < len(visited):
                    if visited[ny+dy][nx+dx] != True and arr[ny+dy][nx+dx] != 0:
                        queue.append([ny+dy, nx+dx])
    return count


n = int(input())
arr = []
visited = [[False for _ in range(n)] for _ in range(n)]
fields = []
for _ in range(n):
    arr.append(list(map(int, list(str(input())))))

for y in range(n):
    for x in range(n):
        if visited[y][x] == True:
            continue
        if arr[y][x] != 0:
            fields.append(search(visited, arr, x, y))
        visited[y][x] = True
fields.sort()
print(len(fields))
for a in fields:
    print(a)
