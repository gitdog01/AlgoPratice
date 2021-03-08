answers = []
while True :
    buf = str(input())
    if buf == '.' :
        break
    stack = []
    
    for char in buf :
        if char == '(' or char == '[' :
            stack.append(char)
        elif char == ')' or char == ']' :
            if char == ')' :
                if len(stack) > 0 and stack[-1] == '(' :
                   stack.pop()
                else :
                    stack.append(char)
            elif char == ']' :
                if len(stack) > 0 and stack[-1] == '[' :
                    stack.pop()
                else :
                    stack.append(char)
    if len(stack) == 0 :
        answers.append("yes")
    else :
        answers.append("no")

for answer in answers :
    print(answer)