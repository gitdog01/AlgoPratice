import sys


class Node:
    def __init__(self, head, left='.', right='.') -> None:
        self.name = head
        if left == '.':
            self.left = None
        else:
            self.left = Node(left)

        if right == '.':
            self.right = None
        else:
            self.right = Node(right)


class Tree:
    def __init__(self, root) -> None:
        self.root = root

    def add(self, new_node):
        queue = [self.root]
        while queue:

            now = queue.pop()
            if now.name == new_node.name:
                now.left = new_node.left
                now.right = new_node.right
                return
            else:
                if now.left != None:
                    queue.append(now.left)
                if now.right != None:
                    queue.append(now.right)

    def pre_print(self, root):
        now = root
        print(now.name, end='')
        if now.left != None:
            self.pre_print(now.left)
        if now.right != None:
            self.pre_print(now.right)

    def mid_print(self, root):
        now = root
        if now.left != None:
            self.mid_print(now.left)
        print(now.name, end='')
        if now.right != None:
            self.mid_print(now.right)

    def back_print(self, root):
        now = root
        if now.left != None:
            self.back_print(now.left)
        if now.right != None:
            self.back_print(now.right)
        print(now.name, end='')


def solve():
    N = int(sys.stdin.readline().replace("\n", ""))
    mTree = None

    for _ in range(N):
        head, left, right = sys.stdin.readline().replace("\n", "").split()
        if mTree == None:
            mTree = Tree(Node(head, left, right))
        else:
            mTree.add(Node(head, left, right))
    mTree.pre_print(mTree.root)
    print()
    mTree.mid_print(mTree.root)
    print()
    mTree.back_print(mTree.root)
    print()


solve()
