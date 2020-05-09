def solution(answers):
    answer = []
    
    supo1 = [1,2,3,4,5] # 5
    supo2 = [2,1,2,3,2,4,2,5] # 8
    supo3 = [3,3,1,1,2,2,4,4,5,5] # 10
    
    supo1_score = 0
    supo2_score = 0
    supo3_score = 0
    
    answer_long = len(answers)
    
    supo1_sheet = supo1*(answer_long//5)
    supo2_sheet = supo2*(answer_long//8)
    supo3_sheet = supo3*(answer_long//10)
    
    for ext in range(answer_long%5) :
        supo1_sheet.append(supo1[ext])
    for ext in range(answer_long%8) :
        supo2_sheet.append(supo2[ext])
    for ext in range(answer_long%10) :
        supo3_sheet.append(supo3[ext])
    
    for i in range(len(answers)) :
        if supo1_sheet[i] == answers[i] :
            supo1_score = supo1_score + 1
    for i in range(len(answers)) :
        if supo2_sheet[i] == answers[i] :
            supo2_score = supo2_score + 1
    for i in range(len(answers)) :
        if supo3_sheet[i] == answers[i] :
            supo3_score = supo3_score + 1

    if supo1_score != 0 and supo2_score == supo1_score == supo3_score :
        answer = [1,2,3]
    elif supo1_score != 0 and supo1_score == supo2_score :
        answer = [1,2]
    elif supo2_score != 0 and supo2_score == supo3_score :
        answer = [2,3]
    elif supo3_score != 0 and supo3_score == supo1_score :
        answer = [1,3]
    else :
        scores.append(supo1_score)
        scores.append(supo2_score)
        scores.append(supo3_score)
        answer.append(1+scores.index(max(scores)))


    print(answer)
    return answer
answers = [1,3,2,4,2]
solution(answers)