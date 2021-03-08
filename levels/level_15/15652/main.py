N,M = map(int,input().split())
check = [False] * N
out = []

def go(lv,idx,out) :
    if lv == M :
        for num in out :
            print(num,end=" ")
        print()
        return
    for a in range(idx,N) :
        out.append(a+1)
        go(lv+1,a,out)
        out.pop()

go(0,0,out)
