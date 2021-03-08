N,T = map(int,input().split())

total = 0
coin = []
for a in range(N) :
    coin.append(int(input()))
for i in range(len(coin)-1,-1,-1) :
    temp = T//coin[i]
    if  temp > 0 :
        total += temp
        T -= temp*coin[i]
print(total)
#00:10:31