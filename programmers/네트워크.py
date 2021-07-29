#최종적으로 Tree가 몇개인지 찾는 문제 

def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    def dfs(node, network):

        for i in range(len(network)):
            if network[i] == 1:
                if visited[i] == 1:
                    continue
                else:
                    visited[i] = 1
                    dfs(i, computers[i])

        return True
                
    
    while not all(visited):
        place = visited.index(0)
        answer += dfs(place, computers[place])
    
    return answer
