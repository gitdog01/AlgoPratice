#hanoE_py
def hanoi(n,s_p,h_p,e_p) :
    if n == 1 :
        print(s_p,e_p)
        return
    hanoi(n-1,s_p,e_p,h_p)
    print(s_p,e_p)
    hanoi(n-1,h_p,s_p,e_p)

n = int(input())
print(2**n-1)
hanoi(n,1,2,3)