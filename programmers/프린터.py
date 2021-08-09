from collections import OrderedDict

def solution(priorities, location):
    answer = 0
    queue = OrderedDict(zip(range(len(priorities)), priorities)) ##location : priorities

    while queue:
        i, pri = list(queue.items())[0]
        
        if pri >= max(queue.values()):
            queue.popitem(last=False) #맨 앞 pop
            answer += 1
            if i == location:
                break
                
        else:
            queue.move_to_end(i, last=True) #맨 뒤로 보낸다
    
    return answer



### deque, any 사용 
from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque(list(zip(range(len(priorities)), priorities)))
    
    while queue:
        i, pri = queue.popleft()
        
        if any(pri < tmp[1] for tmp in queue): 
            queue.append((i,pri))
        else:
            answer += 1
            if i == location:
                break
                
    return answer
