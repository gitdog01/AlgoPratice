import sys
N = int(sys.stdin.readline().replace("\n", ""))
chu = sorted(list(map(int, sys.stdin.readline().replace("\n", "").split())))

answer = 1
for c in chu:
    if answer < c:
        break
    answer += c
print(answer)
