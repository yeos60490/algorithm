class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 :
            return ""
        elif len(strs) == 1:
            return strs[0]
            
            
        common = ""
        strs.sort()
        for x, y in zip(strs[0], strs[-1]):
            if x == y:
                common += x
            else:
                break
                
        '''
        for i in range(len(min(strs))):
            if all(strs[0][i] == each[i] for each in strs):
                common += strs[0][i]
            else:
                break
        '''
        
        return common
