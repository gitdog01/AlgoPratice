import sys
X, Y = map(int, sys.stdin.readline().replace("\n", "").split(" "))
maze = []
for _ in range(Y):
    maze.append(list(sys.stdin.readline().replace("\n", "")))
