import sys
# 시간 초과를 해결하는 방법이 잘 떠오르질 않아서 정답을 보고 공부했습니디.
import collections

T = int(sys.stdin.readline().replace("\n", ""))
for i in range(T):
    first, second, third = map(
        list, sys.stdin.readline().replace("\n", "").split(" "))

    sizeA = len(first)
    sizeB = len(second)
    sizeC = sizeA+sizeB
    queue = collections.deque([[-1, -1, 0, ""]])
    visited = [[False for _ in range(sizeB+1)]
               for _ in range(sizeA+1)]
    visited[0][0] = True
    answer = 'no'

    while queue:
        a, b, c, word = queue.popleft()
        if c == sizeC:
            answer = 'yes'
            break
        if a+1 < sizeA and third[c] == first[a+1] and visited[a+2][b+1] == False:
            queue.append([a+1, b, c+1, word+first[a]])
            visited[a+2][b+1] = True
        if b+1 < sizeB and third[c] == second[b+1] and visited[a+1][b+2] == False:
            queue.append([a, b+1, c+1, word+second[b]])
            visited[a+1][b+2] = True
    print("Data set %d: %s" % (i+1, answer))
