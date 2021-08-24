## https://programmers.co.kr/learn/courses/30/lessons/67256

def distance(num):
    if num == 0: return 0
    elif num in [1,3]: return 1
    elif num in [2,4,6]: return 2
    elif num in [5,7,9]: return 3
    else: return 4
    
def solution(numbers, hand):
    answer = ''
    last_l, last_r = 10, 12

    for i in numbers:
        if i == 0: i = 11
          
        if i in [1,4,7]: answer += 'L'
        elif i in [3,6,9]: answer += 'R'
        else:
            dist_l = distance(abs(i-last_l))
            dist_r = distance(abs(i-last_r))
            
            if dist_l < dist_r: answer += 'L'
            elif dist_l > dist_r: answer += 'R'
            else: answer += hand[0].upper()
        
        if answer[-1] == 'L': last_l = i
        else: last_r = i
            
    return answer
