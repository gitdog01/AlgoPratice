from collections import defaultdict

def solution(tickets):
    answer = []
    graph = defaultdict(list)
    for start, end in tickets : 
        graph[start].append(end) 
    
    for airpot in graph.keys() : 
        graph[airpot].sort()
        
    stack = ["ICN"]
    
    while stack :
        top = stack.pop()
    
        if top not in graph or not graph[top] :
            answer.append(top)
        else:
            stack.append(top)
            stack.append(graph[top].pop(0))
    
    
    return answer[::-1]
