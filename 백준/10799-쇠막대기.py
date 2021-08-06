
from collections import deque

def solution(text):
    text = text.replace("()", "1")
    stack = deque()
    answer = 0

    for i in text:
        if i == ')':
            laser = 0
            prev = stack.pop()
            while prev != '(': ## 쇠막대기 사이의 레이저 개수 구하기 
                laser += int(prev)
                prev = stack.pop()

            stack.append(laser)
            answer += laser + 1

        else:
            stack.append(i)

    return answer
        
if __name__ == '__main__':
    print(solution(input()))
