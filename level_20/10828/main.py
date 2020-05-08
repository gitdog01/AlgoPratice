stack = []
n = int(input())

buf = ""
orders = []
for a in range(n) :
    buf = input()
    orders.append(buf)

for order in orders :

    if "push" in order :
        a,b = order.split()
        stack.append(b)

    if "pop" in order :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack.pop())

    if "size" in order :
        print(len(stack))

    if "empty" in order :
        if len(stack) == 0 : 
            print(1)
        else : 
            print(0)

    if "top" in order :
        if len(stack) == 0 : 
            print(-1)
        else :
            print(stack[-1])


