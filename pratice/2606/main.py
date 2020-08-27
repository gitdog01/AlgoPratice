def worm(com,num,count):
    if visited[num] == True :
        return 0
    visited[num] = True
    count.append(1)
    for i in range(com+1):
        if commap[num][i] == 1 :
            worm(com,i,count)

com = int(input())
connet = int(input())
commap = [[0]*(com+1) for _ in range((com+1))]
visited = [False for _ in range((com+1))]
count = []
for n in range(connet):
    a,b = map(int,input().split(" "))
    commap[a][b] = 1
    commap[b][a] = 1
worm(com,1,count)
print(len(count)-1)