import sys


def find(size, sea, n):
    result = []

    for y in range(n):
        for x in range(n):
            if 0 < sea[y][x] < size:
                result.append([y, x])
    return result


N = int(sys.stdin.readline().replace("\n", ""))
sea = []
shark_size = 2
shark_hungry = 0
now_y = 0
now_x = 0
time = 0
for i in range(N):
    line = list(map(int, sys.stdin.readline().replace("\n", "").split()))
    sea.append(line)
    if line.count(9) == 1:
        now_y = i
        now_x = line.index(9)

state = find(shark_size, sea, N)
while len(state) != 0:
    #print("shark_size", shark_size, "time", time, state)
    #print("now_y", now_y, "now_x", now_x)
    distance = sys.maxsize
    for fy, fx in state:
        dy = abs(fy-now_y)
        dx = abs(fx-now_x)
        far = dy**2 + dx**2
        if distance > far:
            next_y = fy
            next_x = fx
            next_t = dy+dx
            distance = dy+dx
    now_y = next_y
    now_x = next_x
    sea[now_y][now_x] = 0
    time += next_t
    if shark_size > shark_hungry:
        shark_hungry += 1
        if shark_size == shark_hungry:
            shark_size += 1
            shark_hungry = 0
    state = find(shark_size, sea, N)

print(time)
