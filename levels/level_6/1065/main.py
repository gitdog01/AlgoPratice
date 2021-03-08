n = input()

if (int(n) < 100):
    print(n)
elif int(n) == 1000:
    print(144)
else:
    count = 99
    for num in range(100, int(n)+1):
        if int(str(num)[0])-int(str(num)[1]) == int(str(num)[1])-int(str(num)[2]):
            count += 1
    print(count)
