import sys
M, N, B = map(int, sys.stdin.readline().replace("\n").split())
ground = []
for _ in range(N):
    ground.append(list(map(int, sys.stdin.readline().replace("\n").split())))

bottom = 0
top = 256
answer = sys.maxsize
