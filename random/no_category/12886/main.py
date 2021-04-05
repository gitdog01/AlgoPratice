# 1시간 고민하고 보고 품
import sys
sys.setrecursionlimit(100000)


def dfs(stones, visited):
    stones.sort()
    a, b, c = stones
    if a <= 0 or b <= 0 or c <= 0:
        return 0
    if str(a)+"/"+str(b)+"/"+str(c) in visited:
        return 0
    visited[str(a)+"/"+str(b)+"/"+str(c)] = True

    count = 0
    if a == b == c:
        return 1

    # a - > b
    if a != b:
        da = a*2
        db = b-a
        count += dfs([da, db, c], visited)

    # a - > c
    if a != c:
        da = a*2
        dc = c-a
        count += dfs([da, b, dc], visited)

    # b - > c
    if b != c:
        db = b*2
        dc = c-b
        count += dfs([a, db, dc], visited)

    return count


stones = list(map(int, sys.stdin.readline().replace("\n", "").split(" ")))
visited = {}
if sum(stones) % 3 != 0:
    print(0)
else:
    print(dfs(stones, visited))
# print(visited)
