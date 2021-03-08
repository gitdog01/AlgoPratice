import sys
import collections
T = int(sys.stdin.readline().replace("\n", ""))
for _ in range(T):
    N, M = map(int, sys.stdin.readline().replace("\n", "").split(" "))
    stack = list(map(int, sys.stdin.readline().replace("\n", "").split(" ")))
    queue = collections.deque(stack)

    stack.sort()
    count = 0
    now = M
    while queue:
        if stack[-1] == queue[0]:
            count += 1
            if now == 0:
                break
            stack.pop()
            queue.popleft()
            N -= 1
        else:
            back = queue.popleft()
            queue.append(back)
        if now > 0:
            now -= 1
        else:
            now = N-1
    print(count)
