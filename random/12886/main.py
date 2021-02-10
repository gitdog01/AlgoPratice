# 1시간 고민하고 걍 품
import sys
A, B, C = map(int, sys.stdin.readline().replace("\n", "").split(" "))
if sum(A, B, C) % 3 != 0:
    print(0)
visited = []
