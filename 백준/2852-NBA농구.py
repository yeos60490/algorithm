## https://www.acmicpc.net/problem/2852

from datetime import datetime

if __name__ == '__main__':
    last_goal = datetime.strptime("00:00", '%M:%S')
    info = {1: [0,last_goal], 2:[0,last_goal]}     ##팀 : [스코어, 합산시간]

    for i in range(int(input())): ##골
        tmp = input().split(" ")
        score = int(tmp[0])                        ##골을 넣은 팀
        winning = score                            ##이기고 있는 팀
        time = datetime.strptime(tmp[1], '%M:%S')  ##골을 넣은 시간

        score_diff = info[score][0] - info[3-score][0] 
        
        if score_diff < 0:                         ##상대팀이 이기고 있는 경우
            info[3-score][1] += (time - last_goal) 
            winning = 0 if score_diff == -1 else 3-score

        elif score_diff > 0:                       ##우리팀이 이기고 있는 경우
            info[score][1] += (time - last_goal) 

        info[score][0] += 1                        ##스코어 추가
        last_goal = time

    if winning != 0:
        info[winning][1] += (datetime.strptime("48:00", '%M:%S') - last_goal)

    
    print(str(info[1][1].time())[3:])
    print(str(info[2][1].time())[3:])
