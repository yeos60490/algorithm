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
