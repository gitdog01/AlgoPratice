import collections


class node:
    def __init__(self, num):
        self.num = num
        self.child = []


class Tree:
    def __init__(self):
        self.pivet = 0
        self.root = node(-1)

    def add(self, num):
        queue = collections.deque([self.root])
        while queue:
            now = queue.popleft()
            if now.num == num:
                now.child.append(node(self.pivet))
                self.pivet += 1
                return
            else:
                for child in now.child:
                    queue.append(child)

    def delete(self, num):
        queue = collections.deque([self.root])
        while queue:
            now = queue.popleft()
            for i in range(len(now.child)):
                if now.child[i].num == num:
                    now.child.pop(i)
                    return
                else:
                    queue.append(now.child[i])

    def leaf(self):
        queue = collections.deque([self.root])
        count = 0
        while queue:
            now = queue.popleft()
            if len(now.child) == 0 and now.num != -1:
                count += 1
            for child in now.child:
                queue.append(child)

        return count


n = input()
array = list(map(int, input().split()))
d = int(input())

root = Tree()

for i in array:
    root.add(i)
root.delete(d)
print(root.leaf())
