## https://programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    answer = new_id
    
    #step 1
    answer = answer.lower() 
    
    #step 2
    for i in answer:
        if not(i.isdigit() or i.isalpha() or i in ['-','_','.']): 
            answer = answer.replace(i, "") 

    #step 3
    while '..' in answer:
        answer = answer.replace("..", ".")
    
    #step 4
    if answer[0] == ".": 
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == ".": answer = answer[:-1]
    
    #step 5
    if answer == "": answer = "a"
        
    #step 6
    if len(answer) > 15: 
        answer = answer[:15] 
        if answer[-1] == '.':
            answer = answer[:-1]
    
    #step 7
    if len(answer) < 3: 
        answer += answer[-1]*(3-len(answer))
        
    return answer
