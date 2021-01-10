array = []
for _ in range(10):
    array.append((int(input()) % 42))
print(len(set(array)))
