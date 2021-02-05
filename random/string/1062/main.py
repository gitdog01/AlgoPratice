import sys
N, K = map(int, sys.stdin.readline().split(" "))
if K < 5:
    print(0)
else:
    words = dict()
    word_book = []
    can = []
    for _ in range(N):
        word = list(sys.stdin.readline().replace(
            "\n", ""))
        print(word)
        word_book.append(list(set(word)))
        print(list(set(word)))
        for char in word:
            if char not in words:
                words[char] = 0
            words[char] += 1

    def fi(x):
        return words[x]

    print(words)
    words = sorted(words, key=fi)

    while len(can) < K:
        now = words.pop()
        if now not in can:
            can.append(now)
        if len(words) == 0:
            break
    print(can)
