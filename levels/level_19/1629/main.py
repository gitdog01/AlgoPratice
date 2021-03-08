def divide(A, B):
    if(B % 2 > 0):
        return divide(A, B - 1) * A
    elif(B == 0):
        return 1
    elif(B == 1):
        return A
    else:
        result = divide(A, B//2)
        return result ** 2 % C


A, B, C = map(int, input().split(' '))
print(divide(A, B) % C)
