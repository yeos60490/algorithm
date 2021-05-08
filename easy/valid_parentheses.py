class Solution:
    def isValid(self, s: str) -> bool:
        #pair1 = ['{', '[', '(']
        #pair2 = ['}', ']', ')']
        pair = {'}': '{', ']': '[', ')': '('}
        stack = []
        for i in s:
            '''
            if i in pair1:
                stack.append(i)
            elif i in pair2 and len(stack)>0 and stack[-1] == pair1[pair2.index(i)]:
                del stack[-1]
            else:
                return False
            '''
            if i in pair and len(stack)>0 and stack[-1] == pair[i]:
                del stack[-1]
            else:
                stack.append(i)
                
        if len(stack) == 0:
            return True
        else:
            return False
                
