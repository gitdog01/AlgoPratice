import sys
import collections

Y, X = map(int, sys.stdin.readline().replace("\n", "").split(" "))
office = []
for _ in range(Y):
    office.append(
        list(map(int, sys.stdin.readline().replace("\n", "").split(" "))))
queue = collections.deque([])
for y in range(Y):
    for x in range(X):
        if office[y][x] in range(1, 5):
            queue.append([y, x])
        elif office[y][x] == 5:
            for a in range(X):
                if office[y][a] == 0:
                    office[y][a] = "#"
            for b in range(Y):
                if office[b][x] == 0:
                    office[b][x] = "#"
print(queue)
