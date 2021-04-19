import sys


def solve():
    N, M = map(int, sys.stdin.readline().replace("\n", "").split())
    Truth = list(map(int, sys.stdin.readline().replace("\n", "").split()))
    partys = [[] for _ in range(M)]
    for i in range(M):
        p = list(map(int, sys.stdin.readline().replace("\n", "").split()))
        partys[i] = p[1:]
    if Truth[0] == 0:
        return M
    Truth = Truth[1:]
    answer = 0
    for party in partys:
        for person in party:
            if person in Truth:
                Truth = list(set(Truth+party))
                break

    for party in partys:
        if len(set(party) & set(Truth)) == 0:
            answer += 1
    return answer


print(solve())
