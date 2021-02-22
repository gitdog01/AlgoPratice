import sys
N = int(sys.stdin.readline().replace("\n", ""))
stair = []
f = [0]
for _ in range(N):
    stair.append(int(sys.stdin.readline().replace("\n", "")))
if N > 0:
    f.append(stair[0])
if N > 1:
    f.append(max(stair[0] + stair[1], stair[1]))
if N > 2:
    f.append(max(stair[1] + stair[2], stair[0] + stair[2]))

for i in range(3, N):
    f.append(max(f[i-2]+stair[i-1]+stair[i], f[i-1]+stair[i]))
    #print(f[i], stair[i])
    # print(f)
print(f.pop())
