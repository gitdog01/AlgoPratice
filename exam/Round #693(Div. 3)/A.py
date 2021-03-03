import sys
T = int(sys.stdin.readline().replace("\n", ""))
for _ in range(T):
    w, h, n = map(int, sys.stdin.readline().replace("\n", "").split(" "))
    least = 1
    while w % 2 == 0 or h % 2 == 0:
        if w % 2 == 0:
            w = w//2
            least *= 2
        if h % 2 == 0:
            h = h//2
            least *= 2
    if least >= n:
        print("YES")
    else:
        print("NO")
