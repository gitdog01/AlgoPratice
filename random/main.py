import collections
def mString(inp_str) :
    result = True
    for one in inp_str :
        if not one.isalpha() :
            result = False
    return result

def mNumber(inp_num) :
    result = True
    for one in inp_num :
        if not one.isdigit() :
            result = False
    return result

def mNull() :
    return True

def solution(program, flag_rules, commands):
    answer = []
    rules = {}
    functions = {"STRING":mString,"NUMBER":mNumber,"NULL":mNull}
    requires = {"STRING":1,"NUMBER":1,"NULL":0}
    
    for flag_rule in flag_rules :
        flag_name , flag_argument_type = flag_rule.split()
        rules[flag_name] = flag_argument_type
    
    for command in commands :
        queue = collections.deque(command.split())
        buf = []
        now_function = ''
        
        program_check = queue.popleft() == program
        flag_check = True
        require_check = True
        function_result_check = True
        no_call_check = True
        
        while queue :
            now = queue.popleft()
            if str(now[0]) == "-":
                if now in rules :
                    if now_function == '' :
                        now_function = now
                        buf = []
                        continue
                    else :
                        if requires[rules[now_function]] == len(buf) :
                            if not functions[rules[now_function]](buf) :
                                function_result_check = False
                        else :
                            require_check = False
                            continue
                else : 
                    flag_check = False
                    continue
            else :
                if now_function == '' :
                    no_call_check = False
                    break
                buf.append(now)
                
                
        answer.append(program_check and flag_check and function_result_check and require_check and no_call_check)
    return answer