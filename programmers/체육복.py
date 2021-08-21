## https://programmers.co.kr/learn/courses/30/lessons/42862#

def solution(n, lost, reserve):
    answer = n - len(lost)
    lost.sort()
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            answer += 1
        elif i-1 in reserve:
            reserve.remove(i-1)
            answer += 1
        elif i+1 in reserve:
            if i+1 in lost: pass
            else:
                reserve.remove(i+1)
                answer += 1

    return answer
