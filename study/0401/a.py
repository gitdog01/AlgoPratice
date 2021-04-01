import sys

# N 보석수 K 가방수
# M[i] i 무게 V[i] i 가치
#


def solve():
    N, K = map(int, sys.stdin.readline().replace("\n", "").split())
    jewl = {}
    bag = []
    for _ in range(N):
        M, V = map(int, sys.stdin.readline().replace("\n", "").split())
        jewl[M] = V
    for _ in range(K):
        bag.append(int(sys.stdin.readline().replace("\n", "").split()))


print(solve())
