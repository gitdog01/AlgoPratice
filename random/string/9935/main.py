import sys
origin = str(sys.stdin.readline()).replace("\n", "")
bomb = list(sys.stdin.readline().replace("\n", ""))
bomb.reverse()
stack = []
for word in origin:
    stack.append(word)
    # print(stack)
    for idx, r in enumerate(bomb):
        # print('rever', stack[-(idx+1)], r)
        if len(stack) < len(bomb) or stack[-(idx+1)] != r:
            break
        if idx == len(bomb)-1:
            for _ in range(len(bomb)):
                stack.pop()
if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))
