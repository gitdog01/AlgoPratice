import sys
N, K = map(int, sys.stdin.readline().replace("\n", "").split())
# a n t i c
knowledge = {'a', 'n', 't', 'i', 'c'}
new_char = {}
if K < 6:
    print(0)
else:
    for _ in range(N):
        word = sys.stdin.readline().replace("anta", "").replace("tica", "")
