import sys
import copy

N = int(sys.stdin.readline().replace("\n", ""))
first = [i for i in range(1, N+1)]
second = []
queue = []
answer = 0
temp = 0
A = []
B = []
answer_num = []
for i in range(1, N+1):
    num = int(sys.stdin.readline().replace("\n", ""))
    if num != i:
        second.append(num)
    else:
        first.pop(i-1)
        temp += 1

visited = [False for _ in range(N)]

for i in second:
    visited = [False for _ in range(N)]
    queue = [i]
    A = []
    B = []
    while queue:
        now = queue.pop()-1
        A.append(now+1)
        B.append(second[now])
        if visited[now] == False:
            visited[now] = True
            queue.append(second[now])
        else:
            # A.sort()
            # B.sort()
            print("A", A)
            print("B", B)
            if A == B and answer < len(A):
                answer = len(A)
                answer_num = copy.deepcopy(A)
            else:
                break


print()
print(answer+temp)
for num in answer_num:
    print(num)
