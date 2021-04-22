import sys
N, K = map(int, sys.stdin.readline().replace("\n", "").split())
num = list(sys.stdin.readline().replace("\n", ""))
stack = []
count = K
for i in range(N):
    while count > 0 and stack and stack[-1] < num[i]:
        stack.pop()
        count -= 1
    stack.append(num[i])
print(''.join(stack[:N-K]))
print(stack)
