import sys
t = int(sys.stdin.readline().replace("\n", ""))
for _ in range(t):
    n = int(sys.stdin.readline().replace("\n", ""))
    array = list(map(int, sys.stdin.readline().replace("\n", "").split(" ")))
    remainders = []
    goal = len(array)//3
    answer = 0
    c0 = 0
    c1 = 0
    c2 = 0
    for a in array:
        remainder = a % 3
        remainders.append(remainder)
        if remainder == 0:
            c0 += 1
        elif remainder == 1:
            c1 += 1
        else:
            c2 += 1
    answer += abs(c0-goal)  # 2

    # 0
    if c0 > goal:
        temp = c0
        c0 -= abs(temp-goal)
        c1 += abs(temp-goal)
    else:
        temp = c0
        c0 += abs(temp-goal)
        c1 -= abs(temp-goal)
    answer += abs(c1-goal)
    print(answer)
