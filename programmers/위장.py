import collections

def solution(clothes):
    types = list((collections.Counter(c[1] for c in clothes)).values())
    count = len(types)
    
    answer = 1
    for i in range(count):
        answer *= (types[i] + 1) ##개수 + 미착용
        
    return answer-1 ##모두다 안입었을 경우 
