## https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    bucket = [0]
    board = list(map(list, zip(*board))) ##행,열 뒤집기

    for i in moves:
        place = board[i-1]
        
        if place:
            doll = place.pop(0)
            while doll==0:
                doll = place.pop(0)
            
            if bucket[-1] == doll:
                bucket.pop()
                answer += 2
            else:
                bucket.append(doll)
                
    return answer
