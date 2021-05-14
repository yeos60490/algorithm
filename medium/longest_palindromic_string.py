class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        for i in range(len(s)-1):
            target = i
            while True:
                if s[i] in s[target+1:]:
                    target += s[target+1:].index(s[i]) + 1
                    if i == 0:
                        if s[i: target+1] ==  s[target::-1]:
                            if len(longest) < (target+1-i):
                                longest = s[i: target+1] 
                    else:
                        if s[i: target+1] ==  s[target:i-1:-1]:
                            if len(longest) < (target+1-i):
                                longest = s[i: target+1]
                        
                else:
                    break
        
        return longest
                        
        
