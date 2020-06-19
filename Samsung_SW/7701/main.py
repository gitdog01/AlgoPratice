for test_case in range(1, int(input()) + 1):
    words = []
    for test in range(1, int(input()) + 1):
        words.append(input())
    words.sort()
    words = set(words)
    words = sorted(words, key=len)
    type = "#" + str(test_case)
    print(type)
    for temp in words:
        print(temp)