import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque()
    queue.append(math.ceil((100-progresses[0])/speeds[0]))
    
    for i in range(1, len(progresses)):
        days = math.ceil((100-progresses[i])/speeds[i]) ##올림
        if days <= queue[0]:
            queue.append(days)
        else:
            answer.append(len(queue))
            queue.clear()
            queue.append(days)
        
    answer.append(len(queue))
    return answer
