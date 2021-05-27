def solution(array, commands):
    answer = []
    for comm in commands:
        arr = array[comm[0]-1:comm[1]]
        arr.sort()
        answer.append(arr[comm[2]-1])
        
    return answer
