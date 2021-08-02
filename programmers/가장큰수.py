## 사용자 정의 비교문을 사용하여 sort 하기
## functools 의 cmp_to_key 사용
## sorted(array, key=functools.cmp_to_key(func))
## sorted(array, key=lambda x:x[1])


import functools ## cmp_to_key 사용 

def compare(a,b): #사용자 정의 비교 함수
    t1 = a+b
    t2 = b+a
    
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) # t1이 크면 1, t2가 크면 -1, 같으면 0

def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers = sorted(numbers, key=functools.cmp_to_key(compare), reverse=True)
    
    return str(int(''.join(numbers)))

    



## 원래 코드 
'''
from collections import defaultdict

def solution(numbers):
    answer = defaultdict(str)
    max_len = len(str(max(numbers)))
    
    for i in range(len(numbers)):
        string = str(numbers[i])
        
        key = string + string[0] * (max_len-len(string))
        
        if answer[key] + string > string + answer[key]:
            answer[key] = answer[key] + string 
        else: 
            answer[key] = string + answer[key] 
    
    answer = sorted(answer.items(), reverse=True)
    
    return str(int(''.join(dict(answer).values())))
    
'''  
    
