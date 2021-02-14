import sys

N = int(sys.stdin.readline().replace("\n", ""))
first = [i for i in range(1, N+1)]
second = []
queue = []
answer = 0
answer_num = []
for i in range(1, N+1):
    num = int(sys.stdin.readline().replace("\n", ""))
    if num != i:
        second.append(num)
    else:
        first.pop(i-1)
        answer += 1

visited = [False for _ in range(N)]

for i in second:
    queue = [i]

    while queue:
        now = queue.pop()-1

        queue.append(second[now])

print(answer+len(answer_num))
for num in answer_num:
    print(num)
