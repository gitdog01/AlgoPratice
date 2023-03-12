def solution(input_string):
    answer = []
    dic = {}
    last = ''
    for word in list(input_string) :
        if word in dic :
            if last == word :
                last = word
                continue
            else :
                last = word
                if not word in answer :
                    answer.append(word)
            dic[word] += 1
        else :
            last = word
            dic[word] = 1
    answer.sort()
    if ''.join(answer) == "" :
        answer = "N"
    else : 
        answer = ''.join(answer)
    return answer
