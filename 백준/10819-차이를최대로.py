'''
https://www.acmicpc.net/problem/10819

문제
N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.

|A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|


'''
import itertools

def solution(v):
    answer = -1
    pairs = list(itertools.permutations(v,len(v)))

    for p in pairs:
        _sum = 0
        for i in range(1,len(p)):
            _sum += abs(p[i-1] - p[i])
        if _sum > answer:
            answer = _sum

    return answer


if __name__ == '__main__':
    count = input()
    arr = list(map(int, input().split(' ')))
    print(solution(arr))
