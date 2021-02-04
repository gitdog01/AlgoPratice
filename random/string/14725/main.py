import sys


class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.child = dict()


class antAss:
    def __init__(self) -> None:
        self.root = Node()

    def push(self, values):
        now = self.root

        for value in values:
            if value not in now.child:
                now.child[value] = Node(value)
            now = now.child[value]

    def printNode(self, level, node):
        for one in sorted(node.child.keys()):
            print("--"*level, one, sep="")
            self.printNode(level+1, node.child[one])


T = int(sys.stdin.readline().replace("\n", ""))
myHole = antAss()
for _ in range(T):
    words = sys.stdin.readline().replace("\n", "").split(' ')
    myHole.push(words[1:])
myHole.printNode(0, myHole.root)
