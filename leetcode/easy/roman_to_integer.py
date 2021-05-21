class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        for i in range(len(s)):
            if "I" == s[i]:
                if i+1<len(s) and (s[i+1] == "V" or s[i+1] == "X") :
                    num -= 1
                else:
                    num += 1
            elif "V" == s[i]:
                num += 5
            elif "X" == s[i]:
                if i+1<len(s) and (s[i+1] == "L" or s[i+1] == "C") :
                    num -= 10
                else:
                    num += 10
            elif "L" == s[i]:
                num += 50
            elif "C" == s[i]:
                if i+1<len(s) and (s[i+1] == "D" or s[i+1] == "M") :
                    num -= 100
                else:
                    num += 100
            elif "D" == s[i]:
                num += 500
            elif "M" == s[i]:
                num += 1000
                
        return num
