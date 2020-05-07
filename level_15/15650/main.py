N,M = map(int,input().split())
check = [False] * N
out = []

def go(lv,idx,out) :
    if lv == M :
        for num in out :
            print(num,end=" ")
        print()
    for a in range(idx,N) :
        if not check[a] :
            check[a] =True
            out.append(a+1)
            go(lv+1,a+1,out)
            out.pop()
            check[a] =False
        

go(0,0,out)