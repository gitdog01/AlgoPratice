import sys
from _collections import deque
n = int(input())
d = 1
#q = deque()
#for i in range(n) : q.appendleft(int(input()))
q = []
for i in range(n) : q.append(int(sys.stdin.readline()))
answer = ''
stack = []
b = False

while q:
    target = q.pop(0)

    if target >= d:
        for i in range(d,target) :
            stack.append(i)
        answer += ('+' * (target-d+1))
        answer += '-'
        d = target+1
        continue

    try:
        a = stack.index(target)  # 1 2 3 ... 999  1
        answer += ('-'*(len(stack)-a))
        stack = stack[0:a]
    except Exception as e:
        b = True
        break

if b:
    print("NO")
else:
    for i in answer:
        print(i)