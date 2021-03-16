import sys
sys.setrecursionlimit(100000)


def find(y, x, l, maze, answer):
    if maze[y][x] == "0":
        maze[y][x] = "#"
        answer += 1
    point = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    back = [2, 3, 0, 1]
    if l > 0:
        left = l - 1
    else:
        left = 3

    if maze[y+point[left][0]][x+point[left][1]] == "0":
        answer = find(y+point[left][0], x+point[left][1], left, maze, answer)
    elif maze[y][x-1] != "0" and maze[y][x+1] != "0" and maze[y+1][x] != "0" and maze[y-1][x] != "0":

        if maze[y+point[back[l]][0]][x+point[back[l]][1]] != "1":
            answer = find(y+point[back[l]][0], x +
                          point[back[l]][1], l, maze, answer)
        else:
            return answer
    else:
        answer = find(y, x, left, maze, answer)
    return answer


N, M = map(int, sys.stdin.readline().replace("\n", "").split(" "))
R, C, L = map(int, sys.stdin.readline().replace("\n", "").split(" "))
maze = []
for _ in range(N):
    maze.append(list(sys.stdin.readline().replace("\n", "").split(" ")))

print(find(R, C, L, maze, 0))
