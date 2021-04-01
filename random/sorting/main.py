import sys
import heapq


def quickSort(array):
    result = []
    return result


def heapSort(array):
    result = []
    temp = []
    for one in array:
        heapq.heappush(temp, one)
    while temp:
        result.append(heapq.heappop(temp))
    return result


def mergeSort(array):
    result = []
    half = len(array)//2
    if half != 0:
        a = mergeSort(array[:half])
        b = mergeSort(array[half:])
        a_idx = 0
        b_idx = 0

        while a_idx < len(a) or b_idx < len(b):
            if a_idx == len(a):
                for i in range(b_idx, len(b)):
                    result.append(b[i])
                break
            if b_idx == len(b):
                for i in range(a_idx, len(a)):
                    result.append(a[i])
                break

            if a[a_idx] > b[b_idx]:
                result.append(b[b_idx])
                b_idx += 1
            else:
                result.append(a[a_idx])
                a_idx += 1
    else:
        return array
    return result


N = int(sys.stdin.readline().replace("\n", ""))
array = []
for _ in range(N):
    array.append(int(sys.stdin.readline().replace("\n", "")))

# func = heapSort
func = mergeSort


for one in func(array):
    print(one)
