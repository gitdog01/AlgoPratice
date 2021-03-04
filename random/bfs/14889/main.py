import sys
import itertools
N = int(sys.stdin.readline().replace("\n", ""))
S = []
for _ in range(N):
    S.append(list(map(int, sys.stdin.readline().replace("\n", "").split(" "))))

n = [i for i in range(N)]
combis = list(itertools.combinations(n, N//2))
gap = sys.maxsize
for combi in combis:
    enemy = [i for i in n if i not in combi]
    score1 = 0
    score2 = 0
    for x, y in itertools.combinations(enemy, 2):
        score1 += (S[y][x] + S[x][y])
    for x, y in itertools.combinations(combi, 2):
        score2 += (S[y][x] + S[x][y])

    gap = min([gap, abs(score1-score2)])
print(gap)
