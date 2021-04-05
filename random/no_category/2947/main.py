import sys


def change(array):
    if array[0] > array[1]:
        array[0], array[1] = array[1], array[0]
        for a in array:
            print(a, end=" ")
        print()

    if array[1] > array[2]:
        array[1], array[2] = array[2], array[1]
        for a in array:
            print(a, end=" ")
        print()

    if array[2] > array[3]:
        array[2], array[3] = array[3], array[2]
        for a in array:
            print(a, end=" ")
        print()

    if array[3] > array[4]:
        array[3], array[4] = array[4], array[3]
        for a in array:
            print(a, end=" ")
        print()


def check(array):
    for i in range(1, 6):
        if array[i-1] != i:
            return False
    return True


array = list(map(int, sys.stdin.readline().replace("\n", "").split(" ")))
while not check(array):
    change(array)
