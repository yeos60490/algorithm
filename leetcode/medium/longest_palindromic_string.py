 class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s[0]
        
        longest = s[0]
        for i in range(len(s)-1):
            target = i
            while True:
                if s[i] in s[target+1:]:
                    target += s[target+1:].index(s[i]) + 1
                    sub = s[i:target+1]
                    if sub == sub[::-1] and len(longest)<len(sub):
                        longest=sub
                    
                else:
                    break
                    
        return longest
                        
                      
