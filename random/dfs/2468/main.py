import sys
N = int(sys.stdin.readline())
a = []
candi = 0
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]

levels = [0, 1]
for _ in range(N):
    a.append(list(map(int, sys.stdin.readline().split(' '))))
for one in a:
    levels += one
levels = list(set(levels))

for level in levels:
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited_num = 0
    stack = []
    answer = 0
    new = [-1, -1]
    for ty in range(N):
        for tx in range(N):
            if a[ty][tx] > level:
                visited_num += 1
    while visited_num > 0:
        ly = 0
        lx = 0

        for my in range(ly, N):
            for mx in range(lx, N):
                if (a[my][mx] > level) and (visited[my][mx] != True):
                    new = [my, mx]
                    ly = my
                    lx = mx
        visited[new[0]][new[1]] = True
        visited_num -= 1
        stack.append(new)
        while stack:
            now = stack.pop()
            #print(now, 'stack', stack)
            for move in moves:
                dy = now[0] + move[0]
                dx = now[1] + move[1]
                if not ((N > dy >= 0) and (N > dx >= 0)):
                    continue
                if (a[dy][dx] > level) and (visited[dy][dx] != True):
                    stack.append([dy, dx])
                    visited[dy][dx] = True
                    visited_num -= 1
        if new[0] != -1 and new[1] != -1:
            answer += 1
    candi = max(candi, answer)
# print(candi)
print(candi)
