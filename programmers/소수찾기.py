'''
https://programmers.co.kr/learn/courses/30/lessons/42839#

문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

입출력 예
numbers	return
"17"	3
"011"	2

'''

import math
import itertools

def prime(n):
    arr = [True for i in range(n+1)]
    arr[0], arr[1] = False, False
    
    for i in range(2, int(math.sqrt(n))+1):  ##에라토스테네스의 체 -> n의 배수를 모두 false 한다.
        if arr[i] == True:
            j = 2
            while i*j <= n:
                arr[i*j] = False
                j += 1
            
    return arr

def solution(numbers):
    answer = 0
    pairs = set()
    
    for i in range(len(numbers)): ##combinations는 (a,b)만. permutations는 (a,b) (b,a) 둘다 반환
        pairs.update(set(map(''.join, itertools.permutations(numbers, i+1))))
    
    pairs = set(map(int, pairs))
    
    arr = prime(max(pairs))
    for i in pairs:
        answer += arr[i]

    return answer
