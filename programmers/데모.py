'''
직사강형을 만드는 4개의 점중 3개의 점이 주어졌을때,
나머지 하나의 점을 구하는 문제
'''

from collections import Counter

def solution(v):
    x = Counter([x[0] for x in v])
    y = Counter([x[1] for x in v])

    answer = [x.most_common()[-1][0], y.most_common()[-1][0]]
    return answer
