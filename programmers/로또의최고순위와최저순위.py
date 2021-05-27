def solution(lottos, win_nums):
    match = 0
    rand = 0
    rank = [6,6,5,4,3,2,1]
    
    for i in lottos:
        if i in win_nums:
            match += 1
        if i == 0:
            rand += 1
        
    return [rank[match+rand], rank[match]]
