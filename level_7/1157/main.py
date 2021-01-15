line = input().upper()
count = {}
for word in line:
    if count.get(word) == None:
        count[word] = 1
    else:
        count[word] += 1
if list(count.values()).count(count.get(max(count.keys(), key=lambda k: count[k]))) != 1:
    print("?")
else:
    print(max(count.keys(), key=lambda k: count[k]))
