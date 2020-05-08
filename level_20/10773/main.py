n = int(input())
stack = []
for a in range(n) :
    order = int(input())

    if order == 0 :
        if len(stack) != 0 :
            stack.pop()
    else :
        stack.append(order)

total = 0
for i in range(len(stack)) :
    total += stack.pop()

print(total)