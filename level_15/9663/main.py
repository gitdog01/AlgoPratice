import numpy as np
N = int(input())
data = [[False for _ in range(N)] for _ in range(N)]
check = np.array(data)
answers = []
def Queen(depth,x,y,cnt) :

    if depth == N :
        answers.append(cnt)
        return

    if not check[x][y] :
        cnt += 1
        check[:,x] = True
        check[y,:] = True

        for a in range(N) :
            for b in range(N) :
                Queen(depth+1,a,b,cnt)

Queen(0,0,0,0)
print(answers)
            
