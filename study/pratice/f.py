from UserString
import collections


class node:
    def __init__(self, name) -> None:
        self.name = name
        self.child = []


class root:
    def __init__(self) -> None:
        self.root = node("")

    def insert(self, road) -> None:
        now = self.root
        for idx in range(1, len(road)):
            if road[idx] == "":
                break

            if road[idx] not in now.child:
                now.child.append(node(road[idx]))
            else:
                now = now.child

    def delete(self) -> None:
        self.root = node("")

    def mPrint(self) -> None:
        pre = ""
        queue = collections.deque([])
        queue.append([pre, self.root])

        while queue:
            pre, now = queue.popleft()
            buf = pre + "/" + now.name
            print(now.name)
            for next_node in now.child:
                queue.append([buf, next_node])


def solve(directory, command):

    myroot = root()
    for md in directory:
        myroot.insert(md.split("/"))

    for com in command:
        now = com.split(" ")
        if now[0] == "mkdir":
            myroot.insert(now[0])
        elif now[0] == "cp":
            print()
        elif now[0] == "rm":
            print()


directory = [
    "/",
    "/hello",
    "/hello/tmp",
    "/root",
    "/root/abcd",
    "/root/abcd/etc",
    "/root/abcd/hello"
]
command = [
    "mkdir /root/tmp",
    "cp /hello /root/tmp",
    "rm /hello"
]

print(solve(directory, command))
