import collections

array = [5, 4, 3, 2, 1]
collections.deque(array)

for _ in range(len(array)):
    print(array.pop())
