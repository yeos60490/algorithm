'''
https://programmers.co.kr/learn/courses/30/lessons/81302#

문제 설명
개발자를 희망하는 죠르디가 카카오에 면접을 보러 왔습니다.

코로나 바이러스 감염 예방을 위해 응시자들은 거리를 둬서 대기를 해야하는데 개발 직군 면접인 만큼
아래와 같은 규칙으로 대기실에 거리를 두고 앉도록 안내하고 있습니다.

대기실은 5개이며, 각 대기실은 5x5 크기입니다.
거리두기를 위하여 응시자들 끼리는 맨해튼 거리1가 2 이하로 앉지 말아 주세요.
단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다.

예를 들어,
5개의 대기실을 본 죠르디는 각 대기실에서 응시자들이 거리두기를 잘 기키고 있는지 알고 싶어졌습니다. 
자리에 앉아있는 응시자들의 정보와 대기실 구조를 대기실별로 담은 2차원 문자열 배열 places가 매개변수로 주어집니다. 
각 대기실별로 거리두기를 지키고 있으면 1을, 한 명이라도 지키지 않고 있으면 0을 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

제한사항
places의 행 길이(대기실 개수) = 5
places의 각 행은 하나의 대기실 구조를 나타냅니다.
places의 열 길이(대기실 세로 길이) = 5
places의 원소는 P,O,X로 이루어진 문자열입니다.
places 원소의 길이(대기실 가로 길이) = 5
P는 응시자가 앉아있는 자리를 의미합니다.
O는 빈 테이블을 의미합니다.
X는 파티션을 의미합니다.
입력으로 주어지는 5개 대기실의 크기는 모두 5x5 입니다.
return 값 형식
1차원 정수 배열에 5개의 원소를 담아서 return 합니다.
places에 담겨 있는 5개 대기실의 순서대로, 거리두기 준수 여부를 차례대로 배열에 담습니다.
각 대기실 별로 모든 응시자가 거리두기를 지키고 있으면 1을, 한 명이라도 지키지 않고 있으면 0을 담습니다.
'''

from collections import deque 

def search(people, place):
    ch = {'P':0, 'O':1, 'X':2}
    xy = [(1,0),(-1,0),(0,1),(0,-1)]
    check = True
    
    for p in people:
        queue = deque([(p[0],p[1],0,1)]) #x,y,dist,start
        visited = set()
        
        while queue:
            x,y,dist,start = queue.popleft()
            cur = place[x][y]
            dist += ch[cur]
            visited.add((x,y))

            if cur == 'P' and start == 0 and dist in range(0,3):
                check = False
                break
                
            elif dist < 2: #거리가 2보다 작을때만 추가탐색
                for i,j in xy:
                    tmpx,tmpy = x+i, y+j
                    if tmpx in range(0,5) and tmpy in range(0,5) and (tmpx,tmpy) not in visited:
                        queue.append((tmpx,tmpy,dist,0))
                        visited.add((tmpx,tmpy))
        
        if check == False: break
            
    return int(check)
            
    
def solution(places):
    answer = []
    for place in places:
        people = []
        for i in range(len(place)): #P찾기
            for j in range(len(place)):
                if place[i][j] == 'P': people.append((i,j))
        
        answer.append(search(people, place)) #P기준 탐색
        
    return answer
