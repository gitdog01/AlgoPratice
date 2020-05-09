def solution(numbers, hand):
    answer = ''
    left_num = ['1','4','7','*']
    right_num = ['3','6','9','#']
    mid_num = ['2','5','8','0']
    keypad = [['1','2','3'],['4','5','6'],['7','8','9'],['*','0','#']]

    left_pos = '*'
    right_pos = '#'
    
    lx = -1
    ly = -1
    rx = -1
    ry = -1
    nx = -1
    ny = -1

    
    
    for num_int in numbers :
        num = str(num_int)
        if num in left_num :
            left_pos = num
            answer += 'L'
        elif num in right_num :
            right_pos = num
            answer += 'R'
        elif num in mid_num :
            left_distance = 5
            right_distance = 5
            
            for y in range(4) :
                for x in range(3) :
                    
                    if keypad[y][x] == left_pos :
                        lx = x
                        ly = y
                    elif keypad[y][x] == right_pos :
                        rx = x
                        ry = y
                    elif keypad[y][x] == num :
                        nx = x
                        ny = y
            left_distance = abs(lx-nx) + abs(ly-ny)
            right_distance = abs(rx-nx) + abs(ry-ny)
            
            if left_distance > right_distance :
                answer += 'R'
                right_pos = num
            elif right_distance > left_distance :
                answer += 'L'
                left_pos = num
            elif left_distance == right_distance :
                if hand == 'left' :
                    answer += 'L'
                    left_pos = num
                if hand == 'right' :
                    answer += 'R'
                    right_pos = num
    
    return answer