import sys
N, M = map(int, sys.stdin.readline().replace("\n", "").split(" "))

prime = [True] * (M+1)
head = int(M**0.5)

for i in range(2, head+1):
    for j in range(i+i, M+1, i):
        prime[j] = False

prime[1] = False
for i in range(N, M+1):
    if prime[i]:
        print(i)
