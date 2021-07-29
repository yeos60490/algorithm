#최종적으로 Tree가 몇개인지 찾는 문제 

def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    def dfs(node, network):

        for i in range(len(network)): #node 기준 다른 노드에 대해서
            if network[i] == 1: #인접 노드인 경우
                if visited[i] == 1: #이미 방문한 경우
                    continue
                    
                else: #방문 안한 경우
                    visited[i] = 1
                    dfs(i, computers[i]) #방문 안한 노드에 다시 dfs

        return True
                
    
    while not all(visited):
        place = visited.index(0)
        answer += dfs(place, computers[place]) 
    
    return answer
