n = int(input())
already = [1]
node = [0]*(n+1)
for i in range(n-1) :
    a,b = map(int,input().split())
    if a in already :
        already.append(b)
        node[b] = a
    else :
        already.append(a)
        node[a] = b
for i in range(2,n+1):
    print(node[i])