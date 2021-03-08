word = input().upper()
dic = {}
for i in range(0,26) :
    dic[chr(65+i)] = -1

i = 0
for charter in word :
    if dic[charter] == -1 :
        dic[charter] = i
    i+=1

for i in range(0,26) :
    print(dic[chr(65+i)],end=' ')
