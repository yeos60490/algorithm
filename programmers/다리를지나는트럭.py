## https://programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    answer = 1
    curr = [truck_weights.pop(0)]
    queue = [0]
    
    while truck_weights:
        answer += 1
        queue = [sum(i) for i in zip(queue, [1]*len(queue))] ##시간 1초씩 다 더하기

        if queue[0] == bridge_length: ##시간이 지났으면 다리 통과
            queue.pop(0)
            curr.pop(0)

        if sum(curr) + truck_weights[0] <= weight: ##다리가 허용가능한 무게이면 트럭 추가
            curr.append(truck_weights.pop(0))
            queue.append(0)
        
    answer += bridge_length - queue[-1] ##마지막 트럭의 남은 

    return answer
