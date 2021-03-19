import sys


def solve(words):
    open = ["[", "{", "(", "<"]
    close = ["]", "}", ")", ">"]
    stack = []
    answer = 0
    for word in words:
        if word in open:
            stack.append(word)
        elif word in close:
            if len(stack) > 0 and open.index(stack[-1]) == close.index(word):
                stack.pop()
                answer += 1
            else:
                return -1
    return answer


words = sys.stdin.readline().replace("\n", "")
print(solve(words))
