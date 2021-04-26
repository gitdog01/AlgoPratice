import sys
import collections


def bfs(start, v, tree):
    visited = [-1 for _ in range(v+1)]
    queue = collections.deque([start])

    visited[start] = 0
    longest = [0, 0]

    while queue:
        now = queue.popleft()
        for next_v, next_dis in tree[now]:
            if visited[next_v] == -1:
                visited[next_v] = visited[now] + next_dis
                queue.append(next_v)
                if longest[0] < visited[next_v]:
                    longest = visited[next_v], next_v

    return longest


V = int(sys.stdin.readline().replace("\n", ""))
tree = [[] for _ in range(V + 1)]

for _ in range(V):
    line = list(map(int, sys.stdin.readline().replace("\n", "").split()))
    for i in range(1, len(line) - 2, 2):
        tree[line[0]].append((line[i], line[i + 1]))

distance, next_v = bfs(1, V, tree)
distance, next_v = bfs(next_v, V, tree)
print(distance)
