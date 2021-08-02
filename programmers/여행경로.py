## dict 처음 선언할때 type 지정해서 선언 가능
## defaultdict 라이브러리 사용 

from collections import defaultdict

def solution(tickets):
    answer = []
    graph = defaultdict(list)
    
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        graph[ticket[0]].sort()
        
        ## defaultdict 안쓰고 graph = {} 했을 경우 
        ''' 
        if ticket[0] not in graph:
            graph[ticket[0]] = [ticket[1]]
        else:
          graph[ticket[0]].append(ticket[1])
          graph[ticket[0]].sort()
        '''
 
            
    start = 'ICN'
    stack = []
    
    ## dfs 사용 
    ## dfs 순서로 돌면서 stack 을 pop 하면서 answer에 저장 -> answer 역순이 정답
    while graph or stack:
        if start not in graph:
            if not answer:
                answer.append(start)
                
            start = stack.pop()
            answer.append(start)
            
            
        elif graph[start] != []:
            stack.append(start)
            
            if len(graph[start]) == 1:
                start = graph.pop(start)[0] #위치의 마지막 남은 경로인 경우 위치를 graph에서 pop
            else:
                start = graph[start].pop(0) #아직 남은 경로가 있는 경우 해당 경로만 pop
                

    return answer[::-1]

