A = int(input())
B = int(input())
C = int(input())
D = str(A*B*C)
number_dic = {}
for i in range(0,10) :
    number_dic[i] = 0
for char_buf in D :
    char_buf = int(char_buf)
    number_dic[char_buf] = number_dic[char_buf] + 1
for key in number_dic.keys() :
    print(number_dic[key])

