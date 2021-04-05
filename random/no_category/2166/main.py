import sys
N = int(sys.stdin.readline().replace("\n", ""))
xPot = []
yPot = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().replace("\n", "").split(" "))
    xPot.append(x)
    yPot.append(y)

xt = 0
yt = 0
for i in range(N-1):
    xt += xPot[i]*yPot[i+1]
xt += xPot[i+1]*yPot[0]
for i in range(N-1):
    yt += xPot[i+1]*yPot[i]
yt += xPot[0]*yPot[i+1]
print("%.1f" % (abs(xt-yt)/2))
