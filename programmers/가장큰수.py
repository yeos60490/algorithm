## 사용자 정의 비교문을 사용하여 sort 하기
## functools 의 cmp_to_key 사용
## sorted(array, key=functools.cmp_to_key(func))
## sorted(array, key=lambda x:x[1])


###1
import functools ## cmp_to_key 사용 

def compare(a,b): #사용자 정의 비교 함수
    t1 = a+b
    t2 = b+a
    
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) # t1이 크면 1, t2가 크면 -1, 같으면 0

def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers = sorted(numbers, key=functools.cmp_to_key(compare), reverse=True)
    
    return str(int(''.join(numbers)))

    
###2
import functools

def compare(a,b):
    return 1 if int(a+b) > int(b+a) else -1

def solution(numbers):
    numbers = list(map(str,numbers))
    num = sorted(numbers, key=functools.cmp_to_key(compare), reverse=True)
    
    return str(int(''.join(num)))



