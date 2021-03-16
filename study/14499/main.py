import sys
N, M, x, y, k = map(int, sys.stdin.readline().replace("\n", "").split(" "))
maze = []
start = [y, x]
move = [[], [0, 1], [0, -1], [-1, 0], [1, 0]]
dice = [
    [-1, 0, -1],
    [0, 0,  0],
    [-1, 0, -1],
    [-1, 0, -1]
]
dice_y = 3
dice_x = 1
dice_p = 0
for a in range(N):
    maze.append(
        list(map(int, sys.stdin.readline().replace("\n", "").split(" "))))

orders = list(map(int, sys.stdin.readline().replace("\n", "").split(" ")))

ny, nx = start
for order in orders:
    dy, dx = move[order]
    if N > ny + dy > -1 and M > nx + dx > -1:
        if maze[ny+dy][nx+dx] == 0:
            maze[ny+dy][nx+dx] = dice[dice_y][dice_x]
        else:
            dice[dice_y][dice_x] = maze[ny+dy][nx+dx]
            maze[ny+dy][nx+dx] = 0
            # 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다.
            # 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
        print(dice)  # 윗면
    else:
        continue
