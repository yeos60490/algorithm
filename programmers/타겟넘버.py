#list 와 level 로 dfs 구현하기

def solution(numbers, target):
    answer = 0
    
    def dfs(num, level):
        nonlocal answer

        if level == len(numbers):
            #target과 sum 이 같을 경우, answer + 1
            if num == target:
                answer += 1
            return
        
        dfs(num + numbers[level], level+1)
        dfs(num + -1 * numbers[level], level+1)
        

    dfs(0, 0)
    return answer
