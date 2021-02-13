import sys

T = int(sys.stdin.readline().replace("\n", ""))
answer = 0
n = int(sys.stdin.readline().replace("\n", ""))
A = list(map(int, sys.stdin.readline().replace("\n", "").split(" ")))
m = int(sys.stdin.readline().replace("\n", ""))
B = list(map(int, sys.stdin.readline().replace("\n", "").split(" ")))

aSum = [0]
bSum = [0]
temp = 0
for one in A:
    temp += one
    aSum.append(temp)
temp = 0
for one in B:
    temp += one
    bSum.append(temp)
dictA = dict()
for i in range(n+1):
    for j in range(i+1, n+1):
        key = aSum[j]-aSum[i]
        if key not in dictA:
            dictA[key] = 1
        else:
            dictA[key] += 1
for i in range(m+1):
    for j in range(i+1, m+1):
        key = T - (bSum[j]-bSum[i])
        if key in dictA:
            answer += dictA[key]
print(answer)
