import sys
N = int(sys.stdin.readline().replace("\n", ""))
dec = 0

words = []
answer = -1
for _ in range(N):
    word = list(sys.stdin.readline().replace("\n", ""))
    words.append(word)
    dec = max(len(word), dec)

for s in range(len(words)):
    dic = {}
    pivot = 9
    t_words = words[s:] + words[:s]
    for i in range(dec, 0, -1):
        for word in t_words:
            if len(word) >= i:
                if word[len(word)-i] not in dic:
                    dic[word[len(word)-i]] = pivot
                    pivot -= 1
    total = 0
    for word in t_words:
        temp = ""
        for w in word:
            temp += str(dic[w])
        total += int(temp)
    answer = max(total, answer)
print(answer)
