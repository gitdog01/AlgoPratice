N,M = map(int,input().split())
check = [False] * N
out = []

def go(lv,out) :
    if lv == M :
        for num in out :
            print(num,end=" ")
        print()
        return
    for a in range(N) :
        out.append(a+1)
        go(lv+1,out)
        out.pop()        

go(0,out)