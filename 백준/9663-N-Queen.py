'''
https://www.acmicpc.net/problem/9663

문제
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

'''
global visited, n, answer

def check(r,c):
    for i in range(r):
        if abs(r-i)==abs(c-visited[i]):
            return False 

    return True


def solution(r):
    global answer
    if r == n:
        answer += 1
    else:
        for c in range(n):
            if c not in visited[:r]:
                if check(r,c):
                    visited[r]= c
                    solution(r+1)
                else:
                    visited[r]= 0

    return answer



if __name__ == '__main__':
    global visited, n, answer
    n = int(input())
    visited = [0]*n
    answer = 0
    
    print(solution(0))
