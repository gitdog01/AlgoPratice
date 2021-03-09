import sys
king, stone, N = sys.stdin.readline().replace("\n", "").split(" ")

kx = ord(king[0])-65
ky = 8-int(king[1])

sx = ord(stone[0])-65
sy = 8-int(stone[1])

moves = {"R": [0, 1], "L": [0, -1], "B": [1, 0], "T": [-1, 0],
         "RT": [-1, 1], "LT": [-1, -1], "RB": [1, 1], "LB": [1, -1]}

for _ in range(int(N)):
    comand = sys.stdin.readline().replace("\n", "")
    dy, dx = moves[comand]
    if 7 < kx + dx or kx + dx < 0:
        continue
    if 7 < ky + dy or ky + dy < 0:
        continue
    if kx + dx == sx and ky + dy == sy:
        if 7 < sx + dx or sx + dx < 0:
            continue
        if 7 < sy + dy or sy + dy < 0:
            continue
        ky = ky + dy
        kx = kx + dx

        sy = sy + dy
        sx = sx + dx
    else:
        ky = ky + dy
        kx = kx + dx

kx = chr(kx+65)
ky = str(abs(ky-8))
print(kx+ky)

sx = chr(sx+65)
sy = str(abs(sy-8))
print(sx+sy)
# A = 0
# 8 = start
