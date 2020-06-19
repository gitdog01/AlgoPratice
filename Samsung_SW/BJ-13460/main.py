def find(r_x,r_y,b_x,b_y,count):
    if game_board[b_y][b_x] == 'O':
        return
    if game_board[r_y][r_x] == 'O':
        print(count)
        return

    
n,m = map(int,input().split())
game_board = [["0"]*m ]*n
for line in range(n) :
    s = input()
    if s.find('R') != -1:
        red_start = {}
        red_start['x'] = s.find('R')
        red_start['y'] = line
    if s.find('B') != -1:
        blue_start = {}
        blue_start['x'] = s.find('B')
        blue_start['y'] = line
    game_board[line] = s
find(red_start['x'],red_start['y'],blue_start['x'],blue_start['y'],0)
