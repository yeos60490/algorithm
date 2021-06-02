def solution(answers):
    corr = {1:0,2:0,3:0}
    one, len_one = [1,2,3,4,5], 5
    two, len_two = [2,1,2,3,2,4,2,5], 8
    three, len_three = [3,3,1,1,2,2,4,4,5,5], 10

    for i in range(len(answers)):
        if answers[i] == one[int(i%len_one)]:
            corr[1] += 1
        if answers[i] == two[int(i%len_two)]:
            corr[2]  += 1
        if answers[i] == three[int(i%len_three)]:
            corr[3] += 1    
    
    maximum = max(corr.values())
    ans = []
    for i in corr:
        if maximum == corr[i]:
            ans.append(i)
            
    return ans
