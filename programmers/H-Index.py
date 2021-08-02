def solution(citations):
    citations.sort()
    length = len(citations)
    for i in range(length):
        if citations[i] >= length-i:
            return length-i
        
    return 0
  
  
  
'''

def compare(current, after, count_after, count_before):
    for i in reversed(range(current, after+1)):
        if count_after >= i and count_before <= i:
            print
            return i
    
    return -1

def solution(citations):
    citations.sort()
    count = len(citations)
    
    answer = compare(0, citations[0], count, 0)
    for i in range(count-1):
        result = compare(citations[i], citations[i+1], count-(i+1), i)
        answer = result if result > -1 else answer
    
    return answer
'''
