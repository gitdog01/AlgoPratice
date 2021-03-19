import sys
# n^2 으로 해도 괜찮은가 ???


def solve(answer_sheet, sheets):
    polution = [[]for _ in range(len(sheets))]
    for i in range(len(answer_sheet)):
        temp = []
        for j in range(len(sheets)):
            if sheets[j][i] == answer_sheet[i]:
                continue
            else:
                temp.append([j, sheets[j][i]])
