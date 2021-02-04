import sys
T = int(sys.stdin.readline())


class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.child = [None for _ in range(10)]
        self.isEnd = False


class trie:

    def __init__(self) -> None:
        self.root = Node()

    def push(self, values):
        now = self.root
        for value in values:
            if now.isEnd == True:
                return True
            if now.child[value] != None:
                now = now.child[value]
            else:
                new = Node(value)
                now.child[value] = new
                now = new
        now.isEnd = True
        return False


for _ in range(T):
    num = int(sys.stdin.readline())
    root = trie()
    phone_book = []
    for _ in range(num):
        phone = list(map(int, sys.stdin.readline().replace("\n", "")))
        phone_book.append(phone)
    phone_book.sort(key=lambda x: len(x))

    answer = "YES"
    for one in phone_book:
        if root.push(one):
            answer = "NO"
            break
    print(answer)
