## https://www.acmicpc.net/problem/9095

def solution(num):
    if num <= 0: return 0
    elif num == 1: return 1
    elif num == 2: return 2
    elif num == 3: return 4
    else:
        return solution(num-1) + solution(num-2) + solution(num-3)


if __name__ == '__main__':
    for i in range(int(input())):
        print(solution(int(input())))
