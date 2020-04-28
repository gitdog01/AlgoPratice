n = int(input())
def Factorial(number) :
    if number == 1 :
        return 1
    elif number == 0 :
        return 1
    else :
        return number * Factorial(number-1)
print(Factorial(n))