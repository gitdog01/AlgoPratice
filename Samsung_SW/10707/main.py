N = int(input())
Map = []
correct = []
state = 1 # 1: - 2: | 3: \
def move(head,tail,state,N,Map):
    now_x = tail[0]
    now_y = tail[1]
    if state == 3 :
        if map[now_y][now_x] == 1 :
            return
    if tail[0] == N and tail[1] == N:
        correct.append(1)
        return
    # exit
    if state == 1 :
        new_head = [now_x,now_y]
        new_tail = [now_x+1,now_y]
        move(new_head,new_tail,1,N,Map)
        # - 
        new_head = [now_x,now_y]
        new_tail = [now_x+1,now_y+1]
        move(new_head,new_tail,3,N,Map)
        # \

    elif state == 2:
        new_head = [now_x,now_y]
        new_tail = [now_x+1,now_y+1]
        move(new_head,new_tail,3,N,Map)
        # \
        new_head = [now_x,now_y]
        new_tail = [now_x,now_y+1]
        move(new_head,new_tail,2,N,Map)
        # |

    elif state == 3:
        new_head = [now_x,now_y]
        new_tail = [now_x+1,now_y]
        move(new_head,new_tail,1,N,Map)
        # - 
        new_head = [now_x,now_y]
        new_tail = [now_x,now_y+1]
        move(new_head,new_tail,2,N,Map)
        # |
        new_head = [now_x,now_y]
        new_tail = [now_x+1,now_y+1]
        move(new_head,new_tail,3,N,Map)
        # \

    
    
for i in range(N):
    Map.append(input().split())
move([0,0],[1,0],1,N,Map)
