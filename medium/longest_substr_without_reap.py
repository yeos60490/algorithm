class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ""
        longest = 0
        for i in s:
            if i not in substr:
                substr += i
            else:
                substr = substr[substr.index(i)+1:] + i
                
            if len(substr) > longest:
                longest = len(substr) 
                
        return longest
