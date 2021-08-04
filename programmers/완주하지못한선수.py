## del, remove 썼을 경우 효율성에서 통과하지 않았다
## collections 사용하면 빠르다

def solution(participant, completion):
    '''
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    return participant[-1]
    '''
    
    import collections
    
    answer = collections.Counter(participant) - collections.Counter(completion)
    
    return list(answer.keys())[0]
