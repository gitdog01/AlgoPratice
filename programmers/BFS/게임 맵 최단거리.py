def solution(maps):
    
    queu = []
    visited = [[0 for i in range(len(maps[0]))] for j in range(len(maps))] 
    
    answer = -1
    queu.append({ "x":0 , "y":0 , "l":1 })
    direction = [[1,0],[0,1],[-1,0],[0,-1]]
    
    while len(queu) != 0 :
        cur = queu.pop(0)
        if visited[cur["y"]][cur["x"]] == 0 and maps[cur["y"]][cur["x"]] == 1 :
            visited[cur["y"]][cur["x"]] = 1
            for item in direction : 
                n_y = cur["y"] + item[0]
                n_x = cur["x"] + item[1]
                n_l = cur["l"] + 1
                if 0 <= n_y < len(maps) and 0 <= n_x < len(maps[0]) and visited[n_y][n_x] == 0 and maps[n_y][n_x] == 1:
                    queu.append({ "x":n_x , "y":n_y , "l":n_l })
        if cur["y"] == len(maps)-1 and cur["x"] == len(maps[0])-1 :
            answer = cur["l"]
    return answer
