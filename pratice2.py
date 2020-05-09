import re
def solution(expression):
    answer = 0
    answer_list =[]

    possis = [['*','+','-'],['*','-','+'],['+','*','-'],['+','-','*'],['-','*','+'],['-','+','*']]
    
    ori_orders = []
    numbers = re.findall('\d+',expression)
    exp =  re.findall('\D+',expression)
    

    for a in range(len(exp)) :
        ori_orders.append(numbers[a])
        ori_orders.append(exp[a])
    ori_orders.append(numbers[-1])


    for possi in possis :
        orders = ori_orders[:]
        for cal in possi :
            while cal in orders :            
                temp_idx = orders.index(cal)
                temp_a = int(orders[temp_idx-1])
                temp_b = int(orders[temp_idx+1])
                if orders[temp_idx] == '*' :
                    temp_total = temp_a * temp_b
                if orders[temp_idx] == '+' :
                    temp_total = temp_a + temp_b
                if orders[temp_idx] == '-' :
                    temp_total = temp_a - temp_b
                del orders[temp_idx-1]
                del orders[temp_idx-1]
                del orders[temp_idx-1]
                orders.insert(temp_idx-1,temp_total)
        answer_list.append(abs(int(orders[0])))
    print(answer_list)
    return answer

expression = "100-200*300-500+20"
solution(expression)