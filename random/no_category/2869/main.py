import sys
A, B, V = map(int, sys.stdin.readline().replace("\n", "").split())

last = V - A
answer = last // (A-B)
if last % (A-B) != 0:
    answer += 1
print(answer+1)
