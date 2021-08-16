## https://www.acmicpc.net/problem/9375

from collections import Counter

if __name__ == '__main__':

    for i in range(int(input())): ##테스트케이스
        clothes = Counter()

        for j in range(int(input())): ##의상 수
            clothes += Counter([input().split(" ")[1]])
            
        answer = 1
        for c in clothes.values(): ##경우의 수
            answer *= (c+1)

        print(answer-1)
