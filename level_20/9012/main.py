n = int(input())
stack = []
orders = []
for i in range(n) :
    buf = str(input())
    orders.append(buf)

for order in orders :
    for char in order :
        stack.append(char)
        if len(stack) > 1 and char == ")" and stack[len(stack)-2] == "(" :
            stack.pop()
            if len(stack) > 0:
                stack.pop()



    if len(stack) == 0 :
        print("YES")
    else :
        print("NO")
    stack = []
