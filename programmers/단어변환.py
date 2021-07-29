#단어를 한글자 다른걸로 바꿔서 target을 최단 경로로 맞추는 것
#dfs가 아닌 bfs 사용 

def solution(begin, target, words):
    if target not in words:
        return 0 
    
    queue = [(begin, 0)]
    visited = []
    
    while queue:
        node = queue[0][0] #단어
        level = queue[0][1] #깊이 (최단거리)
        queue = queue[1:]
        
        #print("node", node, " level", level, " queue", queue)
        
        visited.append(node)
        if node == target: #타겟 단어이면 리턴
            return level 
        
        for i in range(len(begin)):
            for word in words:
                if word in visited:
                    pass
                elif node[:i] + node[i+1:] == word[:i] + word[i+1:]:
                    queue.append((word,level+1))
                    
        
    return level
