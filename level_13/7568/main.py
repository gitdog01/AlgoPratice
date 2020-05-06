n = int(input())
list = []

for i in range(0,n) :
    w , h = map(int,input().split())
    list.append([w,h])

answer = ""
for b in list :
    rank = 1
    for a in list :
        if a[0] == b[0] and a[1] == b[1] : continue
        if a[0] > b[0] and a[1] > b[1] : rank += 1
    print(rank,end=" ")