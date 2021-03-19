def solve(snapshots, transactions):
    my_snap = {}
    my_tran = [False for _ in range(len(transactions))]

    for snap in snapshots:
        my_snap[snap[0]] = int(snap[1])

    for tran in transactions:
        if my_tran[int(tran[0])]:
            continue
        else:
            my_tran[int(tran[0])] = True
            if tran[2] not in my_snap:
                my_snap[tran[2]] = 0

            if tran[1] == "SAVE":
                my_snap[tran[2]] += int(tran[3])
            else:
                my_snap[tran[2]] -= int(tran[3])
    result = []
    for key in my_snap:
        result.append([key, my_snap[key]])
    return result


snapshots = [

    ["ACCOUNT1", "100"],

    ["ACCOUNT2", "150"]

]

transactions = [

    ["1", "SAVE", "ACCOUNT2", "100"],

    ["2", "WITHDRAW", "ACCOUNT1", "50"],

    ["1", "SAVE", "ACCOUNT2", "100"],

    ["4", "SAVE", "ACCOUNT3", "500"],

    ["3", "WITHDRAW", "ACCOUNT2", "30"]

]
print(solve(snapshots, transactions))
