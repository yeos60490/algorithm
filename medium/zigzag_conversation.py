class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows<2:
            return s

        pattern = numRows*2-2
        output = ['']*pattern
        for i in range(len(s)):
            place = i%pattern
            if place >= numRows:
                place = pattern-place
            output[place] += s[i]

        return ''.join(output)

