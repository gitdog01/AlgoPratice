import sys
import copy


def dfs(words, length, now, answer, answers, moja):
    if len(answer) == length and moja[0] >= 1 and moja[1] >= 2:
        answers.append(answer)
        return
    for idx in range(now+1, len(words)):
        next = copy.deepcopy(moja)
        if words[idx] in ('a', 'i', 'e', 'o', 'u'):
            next[0] += 1
        else:
            next[1] += 1
        dfs(words, length, idx, answer+words[idx], answers, next)


L, C = map(int, sys.stdin.readline().replace("\n", "").split(' '))
words = list(sys.stdin.readline().replace("\n", "").split(' '))
words.sort()
answers = []
moja = [0, 0]
dfs(words, L, -1, '', answers, moja)
for one in answers:
    print(one)
