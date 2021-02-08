import sys


N, K = map(int, sys.stdin.readline().split(' '))

knapsack = [[0 for _ in range(K+1)] for _ in range(N+1)]

W = []
V = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split(' '))
    W.append(a)
    V.append(b)


for i in range(N+1):
    for w in range(K+1):
        if i == 0 or w == 0:
            knapsack[i][w] = 0
        elif W[i-1] <= w:
            knapsack[i][w] = max(V[i-1]+knapsack[i-1]
                                 [w-W[i-1]], knapsack[i-1][w])
        else:
            knapsack[i][w] = knapsack[i-1][w]
print(knapsack[N][K])
