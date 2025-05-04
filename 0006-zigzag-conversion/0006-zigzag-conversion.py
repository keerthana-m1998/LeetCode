class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = []
        cycle = 2 * (numRows-1)
        for r in range(numRows):
            for i in range(r,len(s),cycle):
                result.append(s[i])
                if r != 0 and r != numRows-1 and i+cycle-2*r<len(s):
                    result.append(s[i+cycle-2*r])
        return "".join(result)
        