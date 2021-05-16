#작업중
'''
test case
"aa"
"a"
"aa"
"a*"
"ab"
".*"
"aab"
"c*a*b"
"mississippi"
"mis*is*p*."
"abc"
"a*c"
"abc"
"a.c"
"aaa"
"a*"
"aaa"
"a."
"aab"
"a*."
"aab"
"a*"
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        print(p)
        while p[0] != '.' and p[0] != s[0] and p[1] == "*":
            p = p[2:]
        
        #print(p)
        j = 0
        for i in range(len(p)):
            #j += 1
            print("i: ", i, p[i])
            print("j: " , j, s[j])
            if p[i] == s[j]:
                j += 1
                #print(1)
            elif p[i] == ".":
                j += 1
                #print(2)
            elif p[i] == "*":
                while p[i-1] == s[j]:
                    if j == len(s)-1:
                        print("out")
                        break
                    j += 1
                    
            else:
                #print(4)
                return False
            
            
            
        if j < len(s)-1:
            return False
        else:
            return True
                
            
