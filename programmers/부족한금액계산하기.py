def solution(price, money, count):  
    for i in range(count):
        money -= price*(i+1)
        
    return -1*money if money < 0 else 0
