import sys
# 로봇이 어떤 칸에 올라가거나 이동하면 그 칸의 내구도는 즉시 1만큼 감소한다.


N, K = map(int, sys.stdin.readline().replace("\n", "").split())
belt = list(map(int, sys.stdin.readline().replace("\n", "").split()))
robot = [False for _ in range(2*N)]
answer = 0

while belt.count(0) < K:
    answer += 1
    #print("ori :", belt, robot)

    # 벨트가 한 칸 회전한다.
    belt = [belt[-1]] + belt[:2*N-1]
    robot = [robot[-1]] + robot[:2*N-1]

    #print("belt:", belt, robot)
    # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    for i in range(N-1, -1, -1):
        if robot[i] == True:
            if i == N-1:
                robot[i] = False
                # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
            elif robot[i] == True and robot[i+1] == False and belt[i+1] > 0:
                robot[i+1] = True
                robot[i] = False
                belt[i+1] -= 1
    #print("move:", belt, robot)

    # 올라가는 위치에 로봇이 없다면 로봇을 하나 올린다.
    if robot[0] == False and belt[0] > 0:
        robot[0] = True
        belt[0] -= 1

    #print("new :", belt, robot)
    # 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.


print(answer)
