import sys
import collections


def find(island, now, end, limit, n):
    visited = [False for _ in range(n+1)]
    visited[now] = True
    queue = collections.deque([now])

    while queue:
        now = queue.popleft()
        if now == end:
            return True
        for next_island in island[now]:
            if island[now][next_island] >= limit and visited[next_island] == False:
                visited[next_island] = True
                queue.append(next_island)
    return False


def binary(m_max, island, start, end, n):
    left = 1
    right = m_max
    answer = 0
    while left <= right:
        mid = (left+right) // 2
        # print("if weight is", mid, "l", left, "r", right)
        if find(island, start, end, mid, n):
            # print("poss")
            answer = max(answer, mid)
            left = mid + 1
        else:
            # print("imposs")
            right = mid - 1
    return answer


N, M = map(int, sys.stdin.readline().replace("\n", "").split())
island = {}
m_max = 0
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().replace("\n", "").split())
    m_max = max(C, m_max)
    if A not in island:
        island[A] = {}
    if B not in island:
        island[B] = {}
    island[A][B] = C
    island[B][A] = C


start, end = map(int, sys.stdin.readline().replace("\n", "").split())
print(binary(m_max, island, start, end, N))
