class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sl = s.split()
        return len(sl[-1]) if len(sl) != 0 else 0
    
                
