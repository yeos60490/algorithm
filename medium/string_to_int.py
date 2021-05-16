class Solution:
    def myAtoi(self, s: str) -> int:
        start = 0
        num = 0
        neg = 1

        try:
            num = int(s)
        except:
            for i in s:
                if i <= "9" and i >= "0":
                    start = 1
                    num = num*10 + int(i)
                elif i == "-" and num == 0 and start == 0:
                    start = 1
                    neg = -1
                elif i == "+" and num == 0 and start == 0:
                    start = 1
                elif i == " " and start == 0:
                    continue
                else:
                    break
                    
            num = num*neg
        
        
        if num < (-2)**31:
            return (-2)**31
        elif num > (2)**31-1:
            return (2)**31-1
        else:
            return num
