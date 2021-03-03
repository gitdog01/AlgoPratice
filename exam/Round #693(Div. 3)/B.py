import sys
T = int(sys.stdin.readline().replace("\n", ""))
for _ in range(T):
    n = int(sys.stdin.readline().replace("\n", ""))
    candi = list(map(int, sys.stdin.readline().replace("\n", "").split(" ")))
    total = sum(candi)
    if total % 2 == 1:
        print("NO")
        continue
    two = candi.count(2)
    one = len(candi) - two

    if (two % 2 == 0 and one % 2 == 0) or (two % 2 == 1 and one % 2 == 0 and one >= 2):
        print("YES")
    else:
        print("NO")
