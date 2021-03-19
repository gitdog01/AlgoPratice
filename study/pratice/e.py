def solve(dataSource, tags):

    result = {}
    for data in dataSource:
        for idx in range(1, len(data)):
            if data[idx] not in result:
                result[data[idx]] = []
            result[data[idx]].append(data[0])

    total = []

    for tag in tags:
        total += result[tag]
    total.sort()
    answers = []

    last = ""
    limit = 10
    for one in total:
        if last != one:
            answers.append(one)
            last = one
            limit - 1
        if limit == 0:
            break
    return answers


dataSource = [
    ["doc1", "t1", "t2", "t3"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"]
]
tags = [
    "t1", "t2", "t3"
]
print(solve(dataSource, tags))
