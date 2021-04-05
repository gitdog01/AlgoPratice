import sys


def bfs(array, i, visited, word, answers):
    if i == len(array):
        answers.append(word)
        return
    for a in range(10):
        if visited[a] == False:
            if len(word) == 0:
                visited[a] = True
                bfs(array, i+1, visited, word+str(a), answers)
                visited[a] = False
            elif array[i] == ">" and int(word[-1]) > a:
                visited[a] = True
                bfs(array, i+1, visited, word+str(a), answers)
                visited[a] = False
            elif array[i] == "<" and int(word[-1]) < a:
                visited[a] = True
                bfs(array, i+1, visited, word+str(a), answers)
                visited[a] = False


n = input()
array = sys.stdin.readline().replace("\n", "").split()
answers = []
visited = [False for _ in range(10)]
print(array)
bfs(array, -1, visited, '', answers)
answers.sort()
print(answers[-1])
print(answers[0])
