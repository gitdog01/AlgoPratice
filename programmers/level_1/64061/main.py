def solution(board, moves):
    answer = 0
    stack = []
    for move in moves :
        print(move)
        for y in range(len(board[0])) :
            if board[y][move-1] != 0 :
                if len(stack)!=0 and stack[-1] == board[y][move-1] :
                    stack.pop()
                    answer = answer + 2
                else :
                    stack.append(board[y][move-1])
                board[y][move-1] = 0
                break
    return answer
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
moves = [1,5,3,5,1,2,1,4]
solution(board,moves)