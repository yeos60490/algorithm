class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            num = str(x)[1:]
            num = int('-' + num[::-1])
        else:
            num = int(str(x)[::-1])
        if num <= -2**31 or num >= 2**31 -1 :
            return 0
        else:
            return num
